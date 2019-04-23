from data import data
import json


# Loads and returns the default and initial values for the database from the setup json file.
def get_values(fresh):
    with open('setup.json') as f:
        values = json.load(f)
    default = values['Default']
    init = values['Init']
    return default, init


# Inserts the initial values from the setup json file to the database.
def insert_initial_values(conn, handler, INIT):
    for game in INIT['Games']:
        row = (game['StartDate'], int(game['Haunt']), int(game['TrackValue']))
        game_id = int(data.insert_one(conn, handler['Game'], row) - 1) # This is calculating the index to use for Cards, Players, and Tiles.
        cards = list((int(card['GameID']), card['CardName'], card['Type'], card['State']) for card in INIT['Cards'][game_id])
        players = list((int(player['GameID']), player['PlayerName']) for player in INIT['Players'][game_id])
        tiles = list((int(tile['GameID']), tile['TileName'], tile['Floor'], tile['State']) for tile in INIT['Tiles'][game_id])
        data.insert_many(conn, handler['Card'], cards)
        data.insert_many(conn, handler['Player'], players)
        data.insert_many(conn, handler['Tile'], tiles)
    characters = list((int(character['PlayerID']), character['CharacterName'], int(character['TileID']), int(character['Speed']), int(character['Might']), int(character['Sanity']), int(character['Knowledge'])) for character in INIT['Characters'])
    monsters = list((int(monster['TileID']), monster['MonsterName']) for monster in INIT['Monsters'])
    items = list((int(item['TileID']), item['ItemName']) for item in INIT['Items'])
    data.insert_many(conn, handler['Character'], characters)
    data.insert_many(conn, handler['Monster'], monsters)
    data.insert_many(conn, handler['Item'], items)


# Inserts the cards and tiles when a new game is played
def insert_new_game_values(conn, handler, game_id, DEFAULT):
    cards = list((int(game_id), card['CardName'], card['Type'], 'Not Played') for card in DEFAULT['Cards'])
    tiles = list((int(game_id), tile['TileName'], tile['Floor'], 'Not Played') for tile in DEFAULT['Tiles'])
    data.insert_many(conn, handler['Card'], cards)
    data.insert_many(conn, handler['Tile'], tiles)


# Gets all of the character names.
def get_characters(DEFAULT):
    characters = [character['CharacterName'] for character in DEFAULT['Characters']]
    return characters


# Gets all of the tile names.
def get_tiles(DEFAULT):
    tiles = [tile['TileName'] for tile in DEFAULT['Tiles']]
    return tiles


# Gets all of the player names in a given game.
def get_players(conn, handler_key, game_id):
    player_data = data.get_all(conn, handler_key, game_id)
    players = [player[1] for player in player_data]
    return players


# Gets all of the item names.
def get_items(DEFAULT):
    items = [item['ItemName'] for item in DEFAULT['Items']]
    return items


# Gets all of the monster names.
def get_monsters(DEFAULT):
    monsters = [monster['MonsterName'] for monster in DEFAULT['Monsters']]
    return monsters
