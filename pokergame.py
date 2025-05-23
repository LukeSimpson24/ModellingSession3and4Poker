from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):

        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    @property
    def is_flush(self): # checks if all cards have the same suit
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit: # checks the suit and compares it
                return False # not a flush if one card different
        return True #flush

    @property
    def is_full_house(self):
        return self.number_matches == 8 # checks if number of mathcing ranks is 8

    @property
    def number_matches(self):
        matches = 0 #counts how many ranks match in the hand
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        if self.number_matches == 2: # one pair
            return True
        return False

    @property
    def is_two_pair(self):
        return self.number_matches == 4 # two pairs

    @property
    def is_trips(self):
        if self.number_matches == 6: # three of a kind
            return True
        return False

    @property
    def is_quads(self):
        if self.number_matches == 12: # four of a kind
            return True
        return False

    @property
    def is_straight(self): # calculates difference between highest and lowest hand
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4

count = 0 # counts how many hands have been dealt
matches = 0 # tracks the number of straights
while matches < 10: # loops until it finds 10 straights
    deck = Deck() # new deck
    deck.shuffle() # shuffles the deck
    hand = PokerHand(deck) # deals a hand
    if hand.is_straight:
        matches += 1 # increase matches by one
        print(hand)
    count += 1 # after every hand increase count by 1 (straight or not)

print(f"probability of a full straight is {100*matches/count}%") # frequency of straight to come up
