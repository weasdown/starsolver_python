from rpi_card import Card


class Deck:
    def __init__(self):
        self._cards = []
        self.populate()
        print(self._cards)

    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
        cards = []  # Create an empty list of cards
        self._cards = [Card(s, n) for s in suits for n in numbers]


deck = Deck()
