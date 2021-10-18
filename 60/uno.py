from collections import namedtuple

SUITS = "Red Green Yellow Blue".split()
RANKS = ("1 2 3 4 5 6 7 8 9 Skip Reverse".split() + ["Draw Two"]) * 2 + ["0"]
WILD = ["Wild", "Wild Draw Four"] * 4

UnoCard = namedtuple("UnoCard", "suit name")


def create_uno_deck():
    """Create a deck of 108 Uno cards.
    Return a list of UnoCard namedtuples
    (for cards w/o suit use None in the namedtuple)"""
    deck = [UnoCard(suit, name) for suit in SUITS for name in RANKS]
    deck += [UnoCard(None, name) for name in WILD]
    return deck
