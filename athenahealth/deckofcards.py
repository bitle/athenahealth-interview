import requests


class DeckOfCards(object):
    """ Class to represent API of DeckOfCards
    See: http://deckofcardsapi.com/
    """
    BASE_URL = "https://deckofcardsapi.com/api/deck/{deck_id}/{endpoint}"

    def __init__(self):
        """ Initialize new deck class
        """
        super(DeckOfCards, self).__init__()
        self.deck_id = None

        self.new_deck()

    def new_deck(self):
        """ Create new deck of cards """
        endpoint = "shuffle/?deck_count=1"
        deck_id = self.make_request(endpoint).get('deck_id')
        self.deck_id = deck_id

    def draw(self):
        """ Draw a card from the deck """
        endpoint = "draw/?count=1"
        cards_dictionary = self.make_request(endpoint)
        card = cards_dictionary.get('cards')[0]
        value = card.get('value')
        return Card(value)

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
        deck_id = self.deck_id or "new"
        url = base_url.format(deck_id=deck_id, endpoint=endpoint)
        response = requests.get(url)
        return response.json()


class Card(object):
    """ This class will represent a single card """

    def __init__(self, value):
        super(Card, self).__init__()
        self.value = value
