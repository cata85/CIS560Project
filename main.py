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
    games = helpers.get_games(conn, handler['Game'])
    return render_template('index.html', games=games)


# Joins an existing game based on the provided game_id or creates a new one if not provided.
@app.route('/join', methods=['GET', 'POST'])
def join():
    handler_key = handler['Game']
    if request.method == 'POST':
        game_id = request.form['game_select']
        if game_id.isnumeric():
            row = data.get_one(conn, handler_key, game_id)
            if row:
                return redirect(url_for('game', game_id=game_id))
        return redirect(url_for('index'))
    game_id = data.insert_one(conn, handler_key)
    helpers.insert_new_game_values(conn, handler, game_id, config.DEFAULT)
    return redirect(url_for('game', game_id=game_id))


# Generates the requested game page
@app.route('/game/<int:game_id>', methods=['GET'])
def game(game_id, rows=None, column_names=None, players=None, characters=config.CHARACTERS,
        tiles=config.TILES, items=config.ITEMS, monsters=config.MONSTERS):
    players = helpers.get_players(conn, handler['Player'], game_id)
    return render_template('game.html', game_id=game_id, rows=rows, column_names=column_names,
        players=players, characters=characters, tiles=tiles, items=items, monsters=monsters)


# Selects all the rows for the given table.
@app.route('/game/<int:game_id>/select/<string:table>', methods=['GET'])
def select(game_id, table):
    handler_key = handler[table]
    rows = data.get_all(conn, handler_key, game_id)
    column_names = data.get_column_names(handler_key)
    players = helpers.get_players(conn, handler['Player'], game_id)
    characters = config.CHARACTERS
    tiles = config.TILES
    items = config.ITEMS
    monsters = config.MONSTERS
    table_name = table
    return render_template('game.html', game_id=game_id, rows=rows, column_names=column_names,
        players=players, characters=characters, tiles=tiles, items=items, monsters=monsters, table_name=table_name)

# Inserts row for the given table.
@app.route('/game/<int:game_id>/insert/<string:table>', methods=['POST'])
def insert(game_id, table):
    if request.method == 'POST':
        handler_key = handler[table]
        if table == 'Player':
            row = (game_id, request.form['player_name_player'])
            data.insert_one(conn, handler_key, row)
        elif table == 'Character':
            row = (game_id, request.form['player_name_character'], request.form['character_name_character'], request.form['tile_name_character'],
                request.form['speed_character'], request.form['might_character'], request.form['sanity_character'], request.form['knowledge_character'])
            data.insert_one(conn, handler_key, row, game_id)
        elif table == 'Item':
            row = (game_id, request.form['tile_name_item'], request.form['item_name_item'])
            data.insert_one(conn, handler_key, row, game_id)
        elif table == 'Monster':
            row = (game_id, request.form['tile_name_monster'], request.form['monster_name_monster'])
            data.insert_one(conn, handler_key, row, game_id)
    return redirect(url_for('game', game_id=game_id))


# Updates the selected row for a given table.
# TODO: This needs lots of error handling with values sent.
@app.route('/game/<int:game_id>/update/<string:table>', methods=['POST'])
def update(game_id, table):
    if request.method == 'POST':
        handler_key = handler[table]
        if table == 'Game':
            update_game_id = 1 # Needs changed
            row = (update_game_id, request.form['haunt_game'], request.form['track_value_game'])
            data.update(conn, handler_key, row)
        elif table == 'Character':
            update_character_id = 1 # Needs Changed
            row = (update_character_id, request.form['tile_name_character'], request.form['speed_character'], 
                request.form['might_character'], request.form['sanity_character'], request.form['knowledge_character'])
            data.update(conn, handler_key, row)
        elif table == 'Tile':
            update_tile_id = 1 # Needs Changed
            row = (update_tile_id, request.form['floor_tile'], request.form['state_tile'])
            data.update(conn, handler_key, row)
        elif table == 'Item':
            update_item_id = 1 # Needs Changed
            row = (update_item_id, request.form['tile__name_item'])
            data.update(conn, handler_key, row)
        elif table == 'Monster':
            update_monster_id = 1 # Needs Changed
            row = (update_monster_id, request.form['tile__name_monster'])
            data.update(conn, handler_key, row)
        elif table == 'Card':
            update_card_id = 1 # Needs Changed
            row = (update_card_id, request.form['state_card'])
            data.update(conn, handler_key, row)
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
