import requests


class DeckOfCards(object):
    """ Class to represent API of DeckOfCards
    See: http://deckofcardsapi.com/
    """
    BASE_URL = "https://deckofcardsapi.com/api/deck/%s"

    def __init__(self, deck_id):
        """ Initialize new deck class
        :param deck_id: Deck id
        :type deck_id: str
        """
        super(DeckOfCards, self).__init__()
        self.deck_id = deck_id

    @staticmethod
    def new_deck():
        """ Create new deck of cards """
        endpoint = "new/shuffle/?deck_count=1"
        url = DeckOfCards.BASE_URL % endpoint
        response = requests.get(url)
        deck_id = response.json().get('deck_id')
        return DeckOfCards(deck_id)

    def draw(self):
        """ Draw a card from the deck """
        pass

    def reshuffle(self):
        """ Reshuffle the deck """
        pass
