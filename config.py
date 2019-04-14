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
        'Get_One': game.get_one
    },
    'Card': {
        'Create': card.create_table,
        'Drop': card.drop_table
    },
    'Player': {
        'Create': player.create_table,
        'Drop': player.drop_table
    },
    'Tile': {
        'Create': tile.create_table,
        'Drop': tile.drop_table
    },
    'Character': {
        'Create': character.create_table,
        'Drop': character.drop_table
    },
    'Monster': {
        'Create': monster.create_table,
        'Drop': monster.drop_table
    },
    'Item': {
        'Create': item.create_table,
        'Drop': item.drop_table
    }
}                                                          # Handler for all the tables.
FRESH = True                                               # Start database from scratch.
VALUES = helpers.get_values()
SERVER = 'awsrds.cuhsitdkxbpc.us-west-2.rds.amazonaws.com' # SQL Server to connect to.
USER = 'devmaster'                                         # SQL Server user.
PASSWORD = 'shaner26mhixon'                                # SQL Server password.
DB = 'cis560'                                              # SQL Server database to use.

