from athenahealth.deckofcards import NoMoreCardsError, DeckOfCardsError
from athenahealth.game import Game


def main():
    print "Welcome to Deck of Cards game!"

    game = Game()

    while True:
        try:
            input = raw_input("Draw a card or reshuffle or quit [draw]: ")
            if not input or input == "draw":
                card = game.next_card()
                print "Your card is: %s" % card.value
            elif input == "reshuffle":
                print "Your results are: %s" % pretty_results(game.get_results())
                game.reshuffle()
                print "New game started"
            elif input in ["quit", "exit", "q", "bye"]:
                print "Have a good day!"
                break
            elif input == "results":
                print "Your results are: %s" % pretty_results(game.get_results())
            else:
                print "Unrecognized input"
        except NoMoreCardsError:
            print "No more cards left in the deck. Please reshuffle."
        except DeckOfCardsError:
            print "Unexpected error happened. Please retry."


def pretty_results(results):
    result_string = "\n"
    for card, count in results.iteritems():
        result_string += "%s: %d\n" % (card, count)

    return result_string


if __name__ == '__main__':
    main()
