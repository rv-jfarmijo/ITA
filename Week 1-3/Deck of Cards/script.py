from random import shuffle


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []
        for x in suits:
            for y in values:
                self.cards.append(Card(x,y))

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, number):
        count = self.count()
        actual = min([count, number])
        if count == 0:
            raise ValueError('All cards have been dealt')
        dealt = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return dealt

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full decks can be shuffled')
        shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, number):
        return self._deal(number)


d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(d.cards)
card2 = d.deal_card()