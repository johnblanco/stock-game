# export FLASK_APP=flask_app.py;flask run

from flask import Flask, render_template, session, url_for, request
from werkzeug.utils import redirect

import game

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = b'_6#yfdadf2L"F4Q9z\n\xec]/'


@app.route('/', methods=['GET'])
def home():
    if 'game_state' not in session:
        initial_game_state = game.initial_game_state()
        session['game_state'] = initial_game_state

    from icecream import ic
    ic(session['game_state'])
    month = session['game_state']['month']
    spy_price = session['game_state']['spy_prices'][month]
    tecl_price = session['game_state']['tecl_prices'][month]
    return render_template("home.html", game_state=session['game_state'], spy_price=spy_price, tecl_price=tecl_price)


@app.route('/reset_game/', methods=['GET'])
def reset_game():
    session.pop('game_state', None)
    return redirect(url_for('home'))


@app.route('/selection/', methods=['POST'])
def selection():
    selected_option = request.form['selection']
    player = int(request.form['player'])

    game_state = session['game_state']
    game_state['players'][player]['selected_action'] = selected_option
    session['game_state'] = game_state

    return redirect(url_for('home'))


@app.route('/next_month/', methods=['POST'])
def next_month():
    game_state = session['game_state']
    session['game_state'] = game.next_month(game_state)

    return redirect(url_for('home'))
