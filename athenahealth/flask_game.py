from flask import Flask
from flask import render_template
from flask import request

from athenahealth.deckofcards import NoMoreCardsError, DeckOfCardsError
from athenahealth.game import Game

app = Flask(__name__)
game = Game()


@app.route('/')
def index():
    return render_index()


@app.route('/', methods=["POST"])
def form_submit():
    next_move = request.form.get('next-move')
    try:
        if next_move == 'reshuffle':
            game.reshuffle()
        elif next_move == 'draw':
            game.next_card()
        else:
            app.logger.info("Unexpected next move")
    except NoMoreCardsError:
        return render_index(error="No more cards left in the deck")
    except DeckOfCardsError:
        return render_index(error="Unexpected error. Please try again.")

    return render_index()


def render_index(error=None):
    results = []
    for card, count in game.get_results().iteritems():
        results.append((card.value, count))
    return render_template("index.html", results=results, error=error)


if __name__ == "__main__":
    app.run()
