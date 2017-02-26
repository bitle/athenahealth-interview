from athenahealth.deckofcards import DeckOfCards, Card


def test_new_deck_of_cards():
    new_deck = DeckOfCards()

    assert isinstance(new_deck, DeckOfCards)
    assert new_deck.deck_id
    assert new_deck.remaining == DeckOfCards.DECK_SIZE


def test_draw_a_card():
    new_deck = DeckOfCards()
    card = new_deck.draw()
    assert isinstance(card, Card)
    assert card.value


def test_reshuffle():
    new_deck = DeckOfCards()
    deck_id = new_deck.deck_id

    new_deck.draw()
    assert new_deck.remaining == DeckOfCards.DECK_SIZE - 1

    new_deck.reshuffle()
    assert new_deck.remaining == DeckOfCards.DECK_SIZE
    assert new_deck.deck_id == deck_id
