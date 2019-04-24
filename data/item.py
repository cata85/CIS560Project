import pymssql


# Creates the Item table.
def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Item')
        CREATE TABLE Betrayal.Item
        (
            ItemID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            TileID INT NOT NULL FOREIGN KEY
                REFERENCES Betrayal.Tile(TileID),
            ItemName NVARCHAR(32) NOT NULL
        );
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()


# Drops the Item table.
def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Betrayal.Item;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()


# Inserts one Item and returns that ItemID.
def insert_one(conn, row, game_id):
    cursor = conn.cursor()
    item_id = -1
    if row:
        query = f'''
            INSERT INTO Betrayal.Item VALUES {row};
            '''
        cursor.execute(query)
        conn.commit()
        item_id = cursor.lastrowid
    else:
        print('ERROR: Cannot set default values for table Item. Must give foreign key.')
    cursor.close()
    return item_id


# Inserts many Items into Item table.
def insert_many(conn, rows):
    cursor = conn.cursor()
    if rows:
        cursor.executemany('''INSERT INTO Betrayal.Item VALUES (%d, %s)''', rows)
        conn.commit()
    else:
        print('ERROR: You must provide row values for the insert_many method! Can not be left to default!')
    cursor.close()


# Gets one row given a item_id.
def get_one(conn, item_id):
    cursor = conn.cursor()
    query = f'''
        SELECT * 
        FROM Betrayal.Item I
        WHERE I.ItemID = {item_id};
        '''
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    return row


# Gets all the rows from Item table.
def get_all(conn, game_id):
    cursor = conn.cursor()
    query = f'''
        SELECT I.ItemID, T.TileName, I.ItemName
        FROM Betrayal.Item I
            INNER JOIN Betrayal.Tile T ON T.TileID = I.TileID
        WHERE T.GameID = {game_id};
        '''
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


# Gets the column names for the Item table.
def get_column_names():
    return ['ItemID', 'TileName', 'ItemName']


# Updates an element for a specific Item
# the 'setter' parameter will be a string Example: "TileID = 14"
def update(conn, item_id, setter):
    cursor = conn.cursor()
    query = f'''
        UPDATE Betrayal.Monster
        SET {setter}
        WHERE ItemID = {item_id}
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()
