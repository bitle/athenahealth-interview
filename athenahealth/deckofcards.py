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
        deck_id = self.make_request(endpoint).get('deck_id')
        self.deck_id = deck_id

    def draw(self):
        """ Draw a card from the deck """
        pass

    def reshuffle(self):
        """ Reshuffle the deck """
        pass

    def make_request(self, endpoint, base_url=BASE_URL):
        """ Make API request to https://deckofcardsapi.com/

        This method returns parsed json

        :param base_url: Base URL for API calls
        :type base_url: str
        :param endpoint: Specific endpoint for API call
        :type endpoint: str
        :rtype: dict
        """
        url = base_url % endpoint
        response = requests.get(url)
        return response.json()
