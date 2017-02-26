from athenahealth.deckofcards import DeckOfCards, Card


def test_new_deck_of_cards():
    new_deck = DeckOfCards()

    assert isinstance(new_deck, DeckOfCards)
    assert new_deck.deck_id


def test_draw_a_card():
    new_deck = DeckOfCards()
    card = new_deck.draw()
    assert isinstance(card, Card)
    assert card.value
