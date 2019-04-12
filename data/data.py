from data import game
import pymssql


# Gets the connection to the SQL Server.
def get_connection(server, user, password, db):
    conn = pymssql.connect(server=server, user=user, password=password, database=db)
    return conn


def create_tables(conn, handler):
    for table in handler.keys():
        handler[table]['Create'](conn)


def drop_tables(conn, handler):
    for table in handler.keys():
        handler[table]['Drop'](conn)

