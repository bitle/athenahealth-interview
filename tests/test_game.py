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
