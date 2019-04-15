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
        game_id = data.insert_one(conn, handler['Game'], row)
