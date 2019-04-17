import config
from data import data
import flask
from flask import Flask, render_template, redirect, url_for, request, jsonify
import helpers
import json
import signal
import sys


app = Flask(__name__, static_url_path='/static')
conn = data.get_connection(config.SERVER, config.USER, config.PASSWORD, config.DB)
handler = config.HANDLER


# Renders the home page.
@app.route('/')
def index():
    return render_template('index.html')


# Joins an existing game based on the provided game_id or creates a new one if not provided.
@app.route('/join', methods=['GET', 'POST'])
def join():
    handler_key = handler['Game']
    if request.method == 'POST':
        game_id = request.form['gameIDtextbox']
        if game_id.isnumeric():
            row = data.get_one(conn, handler_key, game_id)
            if row:
                return redirect(url_for('game', game_id=game_id))
        return redirect(url_for('index'))
    game_id = data.insert_one(conn, handler_key)
    return redirect(url_for('game', game_id=game_id))


# Generates the requested game page
@app.route('/game/<int:game_id>', methods=['GET'])
@app.route('/game/<int:game_id>/<rows>', methods=['GET'])
def game(game_id, rows=None):
    return render_template('game.html', game_id=game_id, rows=rows)


# Selects all the rows for the given table.
@app.route('/game/<int:game_id>/select/<string:table>', methods=['GET'])
def select(game_id, table):
    handler_key = handler[table]
    conditional = f'WHERE GameID = {game_id}'
    rows = data.get_all(conn, handler_key, conditional)
    return redirect(url_for('game', game_id=game_id, rows=rows))


# Updates the selected row for a given table.
@app.route('/game/<int:game_id>/update/<string:table>', methods=['POST'])
def update(game_id, table):
    handler_key = handler[table]
    setter = request.form['setterTextbox']
    data.update(conn, handler_key, game_id, setter)
    return redirect(url_for('game', game_id=game_id))


# Handles the case when the user presses Ctrl+C.
def signal_handler(sig, frame):
        conn.close()
        sys.exit(0)


if __name__ == '__main__':
    if config.FRESH:
        data.drop_tables(conn, handler)
        data.create_tables(conn, handler)
        helpers.insert_initial_values(conn, handler, config.INIT)
    else:
        data.create_tables(conn, handler)
    signal.signal(signal.SIGINT, signal_handler)
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='localhost')
    