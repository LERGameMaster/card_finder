"""Plateau de jeu et rendu ASCII de la grille."""

import random
import string

HIDDEN_FACE = " ??? "
CELL_WIDTH = 7
GUTTER = 1
MARGIN = 4


class Card(object):
    """Une carte posee sur le plateau."""

    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.face_up = False
        self.matched = False

    def face(self):
        if self.matched:
            return "[%s]" % self.code
        if self.face_up:
            return " %s " % self.code
        return HIDDEN_FACE


class Board(object):
    """Grille de cartes melangees, adressee en coordonnees du type A1."""

    def __init__(self, pairs, columns=4, rng=None):
        rng = rng or random
        deck = []
        for code, name in pairs:
            deck.append(Card(code, name))
            deck.append(Card(code, name))
        rng.shuffle(deck)

        self.cards = deck
        self.columns = columns

    @property
    def rows(self):
        return (len(self.cards) + self.columns - 1) // self.columns

    @property
    def pairs_left(self):
        return sum(1 for card in self.cards if not card.matched) // 2

    def label(self, index):
        """Coordonnee affichee d'une case, par exemple 'B3'."""
        column = index % self.columns
        row = index // self.columns
        return "%s%d" % (string.ascii_uppercase[column], row + 1)

    def parse(self, token):
        """Convertit 'b3' en indice de case, ou None si la saisie est invalide."""
        token = token.strip().upper()
        if len(token) < 2 or not token[0].isalpha() or not token[1:].isdigit():
            return None

        column = string.ascii_uppercase.index(token[0])
        row = int(token[1:]) - 1
        if column >= self.columns or row < 0 or row >= self.rows:
            return None

        index = row * self.columns + column
        if index >= len(self.cards):
            return None
        return index

    def is_selectable(self, index):
        """Une case deja retournee ou deja appariee ne peut pas etre rejouee."""
        card = self.cards[index]
        return not card.matched and not card.face_up

    def reveal(self, index):
        self.cards[index].face_up = True
        return self.cards[index]

    def resolve(self, first, second):
        """Valide ou annule la paire retournee, et renvoie True si elle colle."""
        left = self.cards[first]
        right = self.cards[second]
        if left.code == right.code:
            left.matched = True
            right.matched = True
            return True

        left.face_up = False
        right.face_up = False
        return False

    def is_complete(self):
        return all(card.matched for card in self.cards)

    def render(self):
        """Rendu texte du plateau, pret a etre imprime."""
        lines = [self._header()]
        for row in range(self.rows):
            cells = self._row_cells(row)
            if row == 0:
                lines.append(self._border(len(cells)))
            faces = " ".join("|%s|" % card.face() for card in cells)
            lines.append("%2d  " % (row + 1) + faces)
            lines.append(self._border(len(cells)))
        return "\n".join(lines)

    def _border(self, cell_count):
        return " " * MARGIN + " ".join("+-----+" for _ in range(cell_count))

    def _row_cells(self, row):
        start = row * self.columns
        return self.cards[start:start + self.columns]

    def _header(self):
        header = [" "] * (MARGIN + self.columns * (CELL_WIDTH + GUTTER))
        for column in range(self.columns):
            position = MARGIN + column * (CELL_WIDTH + GUTTER) + CELL_WIDTH // 2
            header[position] = string.ascii_uppercase[column]
        return "".join(header).rstrip()
