import logging
import requests


class DeckOfCards(object):
    """ Class to represent API of DeckOfCards
    See: http://deckofcardsapi.com/
    """
    BASE_URL = "https://deckofcardsapi.com/api/deck/{deck_id}/{endpoint}"
    DECK_SIZE = 52

    def __init__(self):
        """ Initialize new deck class
        """
        super(DeckOfCards, self).__init__()
        self.deck_id = None
        self.remaining = None

        self.new_deck()
        self.log = logging.getLogger(__name__)

    def new_deck(self):
        """ Create new deck of cards """
        endpoint = "shuffle/?deck_count=1"
        deck_dictionary = self.make_request(endpoint)
        self.deck_id = deck_dictionary.get('deck_id')
        self.remaining = deck_dictionary.get('remaining')

    def draw(self):
        """ Draw a card from the deck """
        endpoint = "draw/?count=1"

        if self.remaining <= 0:
            raise NoMoreCardsError("No more cards left in this deck")

        cards_dictionary = self.make_request(endpoint)
        card = cards_dictionary.get('cards')[0]
        card_value = card.get('value')
        cards_remaining = cards_dictionary.get('remaining')
        self.remaining = cards_remaining
        return Card(card_value)

    def reshuffle(self):
        """ Reshuffle the deck """

        self.new_deck()

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
        try:
            response = requests.get(url)
            parsed_json = response.json()
            if not parsed_json.get("success"):
                error = parsed_json.get("error")
                self.log.error("deckofcardsapi.com returned an error. Content: %s", response.text)
                raise DeckOfCardsError("deckofcardsapi.com returned an error: %s" % error)
            return parsed_json
        except DeckOfCardsError:
            raise
        except:
            self.log.exception("Failed to make a request")
            raise DeckOfCardsError("Connection error")


class Card(object):
    """ This class will represent a single card """

    def __init__(self, value):
        super(Card, self).__init__()
        self.value = value

    @property
    def order_value(self):
        order = {
            'ACE': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'JACK': 11,
            'QUEEN': 12,
            'KING': 13
        }
        return order[self.value]

    def __repr__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return hasattr(other, 'value') and self.value == other.value


class DeckOfCardsError(Exception):
    """ Errors related to DeckOfCards API """


class NoMoreCardsError(DeckOfCardsError):
    """ No more cards left in the deck """
