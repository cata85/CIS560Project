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
def insert_one(conn, handler_key, row=None):
    id = handler_key['Insert_One'](conn, row)
    return id


# Inserts many rows into a given table.
def insert_many(conn, handler_key, rows=None):
    handler_key['Insert_Many'](conn, rows)


# Gets one row from a table given an id.
def get_one(conn, handler_key, id):
    row = handler_key['Get_One'](conn, id)
    return row


# Gets all the rows from a table.
def get_all(conn, handler_key, id):
    rows = handler_key['Get_All'](conn, id)
    return rows


# Updates a single element in a column where id is the key, column is a string of the form "ColumnName = value"
def update(conn, handler_key, id, column):
    handler_key['Update'](conn, id, column)
    