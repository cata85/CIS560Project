from data import data
from data import game


# GLOBALS
HANDLER = {
           'Game': {
                    'Create': game.create_table,
                    'Drop': game.drop_table
                   }
          }                                                # Handler for all the tables.
FRESH = True                                               # Start database from scratch.
SERVER = 'awsrds.cuhsitdkxbpc.us-west-2.rds.amazonaws.com' # SQL Server to connect to.
USER = 'devmaster'                                         # SQL Server user.
PASSWORD = 'shaner26mhixon'                                # SQL Server password.
DB = 'cis560'                                              # SQL Server database to use.

