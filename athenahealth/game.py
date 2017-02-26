from collections import OrderedDict

from athenahealth.deckofcards import DeckOfCards


class Game(object):

    def __init__(self, deck_class=DeckOfCards):
        super(Game, self).__init__()
        self.deck = deck_class()
        self.results = dict()

    def next_card(self):
        card = self.deck.draw()

        try:
            self.results[card] += 1
        except KeyError:
            self.results[card] = 1

        return card

    def get_results(self):
        return OrderedDict(sorted(self.results.items(), key=lambda c: c[0].order_value))

    def reshuffle(self):
        self.deck.reshuffle()
        self.results = dict()
