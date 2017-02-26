import requests


class DeckOfCards(object):
    """ Class to represent API of DeckOfCards
    See: http://deckofcardsapi.com/
    """
    BASE_URL = "https://deckofcardsapi.com/api/deck/%s"

    def __init__(self):
        """ Initialize new deck class
        """
        super(DeckOfCards, self).__init__()
        self.deck_id = None

        self.new_deck()

    def new_deck(self):
        """ Create new deck of cards """
        endpoint = "new/shuffle/?deck_count=1"
        url = DeckOfCards.BASE_URL % endpoint
        response = requests.get(url)
        deck_id = response.json().get('deck_id')
        self.deck_id = deck_id

    def draw(self):
        """ Draw a card from the deck """
        pass

    def reshuffle(self):
        """ Reshuffle the deck """
        pass
