"""Chargement des visuels ASCII stockes dans assets/.

Les fichiers sont optionnels : si l'un d'eux manque (copie partielle du depot
dans un executeur en ligne, par exemple), on retombe sur un rendu minimal.
"""

import os

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

FALLBACK_TITLE = "CARD FINDER"
FALLBACK_BACK = "+-----+\n| ??? |\n+-----+"


def load(name, fallback=""):
    """Contenu texte d'un visuel, sans saut de ligne final."""
    path = os.path.join(ASSETS_DIR, name)
    if not os.path.exists(path):
        return fallback
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read().rstrip("\n")


def title():
    return load("title.txt", FALLBACK_TITLE)


def card_back():
    return load("card_back.txt", FALLBACK_BACK)
