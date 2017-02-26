from athenahealth.game import Game


def test_simple_game():
    new_game = Game()
    card = new_game.next_card()
    results = new_game.get_results()

    assert len(results) == 1
    assert card in results
    assert results[card] == 1
