from athenahealth.deckofcards import DeckOfCards


class Game(object):

    def __init__(self):
        super(Game, self).__init__()
        self.deck = DeckOfCards()
        self.results = dict()

    def next_card(self):
        card = self.deck.draw()

        try:
            self.results[card] += 1
        except KeyError:
            self.results[card] = 1

        return card

    def get_results(self):
        return self.results

    def reshuffle(self):
        self.deck.reshuffle()
        self.results = dict()
