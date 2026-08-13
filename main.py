"""Card Finder - jeu de memoire en console."""

import board as board_module
import cards

PAIR_COUNT = 8
COLUMNS = 4
QUIT_WORDS = {"q", "quit", "exit", "stop"}


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


def play():
    deck = cards.draw(PAIR_COUNT)
    board = board_module.Board(deck, COLUMNS)

    while not board.is_complete():
        print("")
        print(board.render())
        print("Paires restantes : %d\n" % board.pairs_left)

        positions = ask_positions(board)
        if positions is None:
            print("Partie abandonnee.")
            return

        first, second = positions
        board.reveal(first)
        board.reveal(second)
        print("")
        print(board.render())

        if board.resolve(first, second):
            print("\nPaire trouvee : %s" % board.cards[first].name)
        else:
            print("\nRate, les cartes sont retournees.")

    print("")
    print(board.render())
    print("\nToutes les paires sont trouvees, bravo !")


if __name__ == "__main__":
    play()
