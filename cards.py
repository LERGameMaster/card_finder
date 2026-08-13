"""Catalogue des cartes utilisees par le jeu.

Chaque carte tient sur trois caracteres pour rester lisible dans une grille
console, avec un nom complet affiche au moment ou la paire est trouvee.
"""

import random

CATALOG = [
    ("VDL", "Vandale"),
    ("PLO", "Pollo"),
    ("NMF", "Namifique"),
    ("MRT", "Marteen Supreme"),
    ("MNY", "Gentle Mates Minny"),
    ("RMT", "Remontada"),
    ("CLM", "Calma"),
    ("BWK", "Bwarks"),
    ("SBG", "Siborg"),
    ("BBD", "Baby Driver"),
    ("GTG", "Gotaga Pose"),
    ("LKF", "Leakof"),
    ("HRT", "L'Heritier"),
    ("MRC", "Mercato"),
    ("CHV", "La Chevaliere"),
    ("CKD", "Cooked"),
    ("TNL", "Tunnel"),
    ("SLY", "Slay"),
    ("M16", "M16"),
    ("KEY", "Keynote"),
    ("LFI", "Lofi Girl"),
    ("PLN", "La Planete"),
    ("ZZZ", "Zzzzzzz"),
    ("BLB", "Blblblbl"),
]

MAX_PAIRS = len(CATALOG)


def draw(pair_count, rng=None):
    """Tire `pair_count` cartes distinctes du catalogue.

    Renvoie la liste des couples (code, nom) sans doublon ; c'est l'appelant
    qui se charge de dupliquer chaque carte pour former les paires.
    """
    if pair_count < 1:
        raise ValueError("il faut au moins une paire")
    if pair_count > MAX_PAIRS:
        raise ValueError("le catalogue ne contient que %d cartes" % MAX_PAIRS)

    rng = rng or random
    return rng.sample(CATALOG, pair_count)


def find_name(code):
    """Nom complet d'une carte a partir de son code."""
    for card_code, name in CATALOG:
        if card_code == code:
            return name
    return code
