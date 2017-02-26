from flask import Flask
from flask import render_template
from flask import request
from flask import g

from athenahealth.deckofcards import NoMoreCardsError
from athenahealth.game import Game

app = Flask(__name__)
game = Game()


@app.route('/')
def index():
    return render_index()


@app.route('/', methods=["POST"])
def form_submit():
    next_move = request.form.get('next-move')
    if next_move == 'reshuffle':
        game.reshuffle()
    elif next_move == 'draw':
        game.next_card()
    else:
        app.logger.info("Unexpected next move")

    return render_index()


def render_index():
    results = []
    for card, count in game.get_results().iteritems():
        results.append((card.value, count))
    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run()
