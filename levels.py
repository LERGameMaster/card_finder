"""Niveaux de difficulte proposes au lancement de la partie."""

LEVELS = [
    {"key": "1", "label": "Facile", "pairs": 6, "columns": 4},
    {"key": "2", "label": "Normal", "pairs": 10, "columns": 5},
    {"key": "3", "label": "Difficile", "pairs": 18, "columns": 6},
]

DEFAULT_KEY = "2"


def by_key(key):
    """Renvoie le niveau correspondant, ou None si la touche est inconnue."""
    for level in LEVELS:
        if level["key"] == key:
            return level
    return None


def default():
    return by_key(DEFAULT_KEY)


def menu():
    """Lignes du menu de selection, pretes a etre imprimees."""
    lines = []
    for level in LEVELS:
        marker = " (defaut)" if level["key"] == DEFAULT_KEY else ""
        lines.append(
            "  %s. %-10s %2d paires sur %d colonnes%s"
            % (level["key"], level["label"], level["pairs"], level["columns"], marker)
        )
    return lines
