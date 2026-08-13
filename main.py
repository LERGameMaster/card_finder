"""Card Finder - jeu de memoire en console."""

import art
import board as board_module
import cards
import levels
import scoring

QUIT_WORDS = {"q", "quit", "exit", "stop"}


def intro():
    print(art.title())
    print("")
    print("Retrouvez toutes les paires. Les cartes face cachee ressemblent a ca :")
    print("")
    print(art.card_back())
    print("")


def ask_level():
    """Affiche le menu et renvoie le niveau choisi."""
    print("Choisissez un niveau :")
    for line in levels.menu():
        print(line)

    raw = input("Niveau > ").strip()
    if not raw:
        return levels.default()

    level = levels.by_key(raw)
    if level is None:
        print("Niveau inconnu, on part sur le niveau par defaut.")
        return levels.default()
    return level


def ask_positions(board):
    """Lit deux coordonnees. Renvoie None si le joueur veut quitter."""
    raw = input("Deux cartes (ex: a1 b3) > ").strip()
    if raw.lower() in QUIT_WORDS:
        return None

    tokens = raw.split()
    if len(tokens) != 2:
        print("Il faut deux coordonnees separees par un espace.\n")
        return ask_positions(board)

    first = board.parse(tokens[0])
    second = board.parse(tokens[1])
    if first is None or second is None:
        print("Coordonnees hors du plateau.\n")
        return ask_positions(board)

    return first, second


def status_line(board, score):
    return "Paires restantes : %d   |   Chrono : %s   |   Score : %d" % (
        board.pairs_left,
        scoring.format_duration(score.elapsed),
        score.total(),
    )


def summary(board, score):
    print("")
    print("=" * 44)
    print("Duree      : %s" % scoring.format_duration(score.elapsed))
    print("Coups      : %d (%d reussis, %d rates)" % (score.turns, score.matches, score.misses))
    print("Precision  : %.0f%%" % score.accuracy)
    print("Bonus temps: %d" % score.time_bonus())
    print("Score final: %d" % score.total())
    print("=" * 44)


def play():
    intro()
    level = ask_level()
    print("\nNiveau %s : %d paires.\n" % (level["label"], level["pairs"]))

    deck = cards.draw(level["pairs"])
    board = board_module.Board(deck, level["columns"])
    score = scoring.ScoreBoard()
    score.start()

    while not board.is_complete():
        print("")
        print(board.render())
        print(status_line(board, score) + "\n")

        positions = ask_positions(board)
        if positions is None:
            score.stop()
            print("Partie abandonnee.")
            summary(board, score)
            return

        first, second = positions
        board.reveal(first)
        board.reveal(second)
        print("")
        print(board.render())

        if board.resolve(first, second):
            score.register_match()
            print("\nPaire trouvee : %s" % board.cards[first].name)
        else:
            score.register_miss()
            print("\nRate, les cartes sont retournees.")

    score.stop()
    print("")
    print(board.render())
    print("\nToutes les paires sont trouvees, bravo !")
    summary(board, score)


if __name__ == "__main__":
    play()
