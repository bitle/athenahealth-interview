from mock import MagicMock, patch

from athenahealth.deckofcards import DeckOfCards, Card
from athenahealth.game import Game


def test_simple_game():
    new_game = Game()
    card = new_game.next_card()
    results = new_game.get_results()

    assert len(results) == 1
    assert card in results
    assert results[card] == 1


def test_game_with_more_cards():
    new_game = Game()
    card1 = new_game.next_card()
    card2 = new_game.next_card()
    card3 = new_game.next_card()
    results = new_game.get_results()

    assert len(results) == 3
    assert card1 in results
    assert card2 in results
    assert card3 in results


def test_reshuffle():
    new_game = Game()
    card = new_game.next_card()
    results = new_game.get_results()

    assert len(results) == 1
    assert card in results
    assert results[card] == 1

    new_game.reshuffle()
    assert len(new_game.get_results()) == 0


def test_sorted_results():
    cards = (Card("QUEEN"), Card("JACK"), Card("2"))

    class DeckOfCardsStub(DeckOfCards):
        counter = 0

        def draw(self):
            card = cards[DeckOfCardsStub.counter]
            DeckOfCardsStub.counter += 1
            return card

    new_game = Game(deck_class=DeckOfCardsStub)
    new_game.next_card()
    new_game.next_card()
    new_game.next_card()
    results = new_game.get_results()

    assert results.popitem(last=False)[0].value == "2"
    assert results.popitem(last=False)[0].value == "JACK"
    assert results.popitem(last=False)[0].value == "QUEEN"


def test_counts():
    cards = (Card("QUEEN"), Card("QUEEN"), Card("2"))

    class DeckOfCardsStub(DeckOfCards):
        counter = 0

        def draw(self):
            card = cards[DeckOfCardsStub.counter]
            DeckOfCardsStub.counter += 1
            return card

    new_game = Game(deck_class=DeckOfCardsStub)
    new_game.next_card()
    new_game.next_card()
    new_game.next_card()
    results = new_game.get_results()

    print results
    assert results[Card("QUEEN")] == 2
    assert results[Card("2")] == 1
