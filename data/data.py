import pymssql


# Gets the connection to the SQL Server.
def get_connection(server, user, password, db):
    conn = pymssql.connect(server=server, user=user, password=password, database=db)
    return conn


# Creates the tables given.
def create_tables(conn, handler):
    for table in handler.keys():
        handler[table]['Create'](conn)


# Drops the tables given in reverse order.
def drop_tables(conn, handler):
    for table in list(handler.keys())[::-1]:
        handler[table]['Drop'](conn)


# Inserts one row and returns the id created.
def insert_one(conn, handler_key, row=''):
    id = handler_key['Insert_One'](conn, row)
    return id
