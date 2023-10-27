# Deck of cards
# https://projects.raspberrypi.org/en/projects/deck-of-cards

# Create a class
class Card:
    def __init__(self, suit, number):
        self._suit = suit  # underscore indicates to not access attribute directly
        self._number = number

    def __repr__(self):
        return self.number + " of " + self.suit

    @property  # create a getter
    def suit(self):
        return self._suit

    @suit.setter  # create a setter
    def suit(self, suit):
        if suit in ["spades", "hearts", "diamonds", "clubs"]:
            self._suit = suit
        else:
            print("That's not a valid suit name!")

    # Challenge: add a getter and setter
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            self._number = number
        else:
            print("That's not a valid number!")
    # Challenge: aces high?


if __name__ == "__main__":
    # Instantiate an object
    my_card = Card("hearts", "6")
    print(my_card)
    my_card.suit = "diamonds"
    print(my_card)
    my_card.suit = "dinosaurs"
    print(my_card)
    my_card.number = "7"
    print(my_card)
    my_card.number = "42"
    print(my_card)
