"""Chronometre et calcul du score d'une partie."""

import time

MATCH_POINTS = 100
MISS_PENALTY = 10
TIME_BONUS_MAX = 200
TIME_BONUS_TARGET = 120.0


def format_duration(seconds):
    """Formate une duree en mm:ss."""
    seconds = int(seconds)
    return "%02d:%02d" % (seconds // 60, seconds % 60)


class ScoreBoard(object):
    """Suit le chrono, les paires trouvees et les erreurs."""

    def __init__(self, clock=time.time):
        self._clock = clock
        self.started_at = None
        self.stopped_at = None
        self.matches = 0
        self.misses = 0

    def start(self):
        self.started_at = self._clock()
        self.stopped_at = None

    def stop(self):
        self.stopped_at = self._clock()

    def register_match(self):
        self.matches += 1

    def register_miss(self):
        self.misses += 1

    @property
    def turns(self):
        return self.matches + self.misses

    @property
    def elapsed(self):
        if self.started_at is None:
            return 0.0
        end = self.stopped_at if self.stopped_at is not None else self._clock()
        return end - self.started_at

    @property
    def accuracy(self):
        if not self.turns:
            return 0.0
        return 100.0 * self.matches / self.turns

    def time_bonus(self):
        """Bonus degressif : plein pot avant TIME_BONUS_TARGET, nul apres le double."""
        if self.started_at is None:
            return 0
        elapsed = self.elapsed
        if elapsed <= TIME_BONUS_TARGET:
            return TIME_BONUS_MAX
        overtime = elapsed - TIME_BONUS_TARGET
        bonus = TIME_BONUS_MAX * (1.0 - overtime / TIME_BONUS_TARGET)
        return max(0, int(bonus))

    def total(self):
        points = self.matches * MATCH_POINTS - self.misses * MISS_PENALTY
        return max(0, points + self.time_bonus())
