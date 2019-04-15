from data import card
from data import character
from data import game
from data import item
from data import monster
from data import player
from data import tile
import helpers


# GLOBALS
HANDLER = {
    'Game': {
        'Create': game.create_table,
        'Drop': game.drop_table,
        'Insert_One': game.insert_one,
        'Insert_Many': game.insert_many,
        'Get_One': game.get_one,
        'Get_All': game.get_all
    },
    'Card': {
        'Create': card.create_table,
        'Drop': card.drop_table,
        'Insert_One': card.insert_one,
        'Insert_Many': card.insert_many,
        'Get_One': card.get_one,
        'Get_All': card.get_all
    },
    'Player': {
        'Create': player.create_table,
        'Drop': player.drop_table,
        'Insert_One': player.insert_one,
        'Insert_Many': player.insert_many,
        'Get_One': player.get_one,
        'Get_All': player.get_all
    },
    'Tile': {
        'Create': tile.create_table,
        'Drop': tile.drop_table,
        'Insert_One': tile.insert_one,
        'Insert_Many': tile.insert_many,
        'Get_One': tile.get_one,
        'Get_All': tile.get_all
    },
    'Character': {
        'Create': character.create_table,
        'Drop': character.drop_table,
        'Insert_One': character.insert_one,
        'Insert_Many': character.insert_many,
        'Get_One': character.get_one,
        'Get_All': character.get_all
    },
    'Monster': {
        'Create': monster.create_table,
        'Drop': monster.drop_table,
        'Insert_One': monster.insert_one,
        'Insert_Many': monster.insert_many,
        'Get_One': monster.get_one,
        'Get_All': monster.get_all
    },
    'Item': {
        'Create': item.create_table,
        'Drop': item.drop_table,
        'Insert_One': item.insert_one,
        'Insert_Many': item.insert_many,
        'Get_One': item.get_one,
        'Get_All': item.get_all
    }
}                                                          # Handler for all the tables.
FRESH = True                                               # Start database from scratch.
DEFAULT, INIT = helpers.get_values(FRESH)                  # Gets the default values and the initial values for the game.
SERVER = 'awsrds.cuhsitdkxbpc.us-west-2.rds.amazonaws.com' # SQL Server to connect to.
USER = 'devmaster'                                         # SQL Server user.
PASSWORD = 'shaner26mhixon'                                # SQL Server password.
DB = 'cis560'                                              # SQL Server database to use.
