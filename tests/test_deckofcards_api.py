from athenahealth.deckofcards import DeckOfCards


def test_new_deck_of_cards():
    new_deck = DeckOfCards()

    assert isinstance(new_deck, DeckOfCards)
    assert new_deck.deck_id
