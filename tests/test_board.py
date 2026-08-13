"""Tests du plateau (python -m unittest discover -s tests)."""

import os
import random
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import board as board_module  # noqa: E402
import cards  # noqa: E402


def build_board(pair_count=6, columns=4, seed=42):
    deck = cards.draw(pair_count, random.Random(seed))
    return board_module.Board(deck, columns, random.Random(seed))


class ParseTest(unittest.TestCase):
    def setUp(self):
        self.board = build_board()

    def test_first_cell(self):
        self.assertEqual(self.board.parse("a1"), 0)

    def test_is_case_insensitive(self):
        self.assertEqual(self.board.parse("B2"), self.board.columns + 1)

    def test_rejects_unknown_column(self):
        self.assertIsNone(self.board.parse("z1"))

    def test_rejects_row_out_of_range(self):
        self.assertIsNone(self.board.parse("a9"))

    def test_rejects_garbage(self):
        for token in ("", "1a", "aa", "  "):
            self.assertIsNone(self.board.parse(token), token)


class LabelTest(unittest.TestCase):
    def test_round_trip(self):
        board = build_board()
        for index in range(len(board.cards)):
            self.assertEqual(board.parse(board.label(index)), index)


class ResolveTest(unittest.TestCase):
    def setUp(self):
        self.board = build_board()
        self.first = 0
        code = self.board.cards[0].code
        self.twin = next(
            index
            for index, card in enumerate(self.board.cards)
            if card.code == code and index != 0
        )

    def test_matching_pair_stays_visible(self):
        self.assertTrue(self.board.resolve(self.first, self.twin))
        self.assertTrue(self.board.cards[self.first].matched)
        self.assertFalse(self.board.is_selectable(self.twin))

    def test_pairs_left_decreases(self):
        before = self.board.pairs_left
        self.board.resolve(self.first, self.twin)
        self.assertEqual(self.board.pairs_left, before - 1)

    def test_failed_pair_is_hidden_again(self):
        other = next(
            index
            for index, card in enumerate(self.board.cards)
            if card.code != self.board.cards[0].code
        )
        self.board.reveal(self.first)
        self.board.reveal(other)
        self.assertFalse(self.board.resolve(self.first, other))
        self.assertTrue(self.board.is_selectable(self.first))


class RenderTest(unittest.TestCase):
    def test_line_count(self):
        board = build_board()
        lines = board.render().split("\n")
        self.assertEqual(len(lines), 1 + board.rows * 2 + 1)

    def test_hides_codes_by_default(self):
        board = build_board()
        self.assertNotIn(board.cards[0].code, board.render())


if __name__ == "__main__":
    unittest.main()
