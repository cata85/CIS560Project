import pymssql


# Creates the Tile table.
def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Tile')
        CREATE TABLE Betrayal.Tile
        (
            TileID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            GameID INT NOT NULL FOREIGN KEY
                REFERENCES Betrayal.Game(GameID),
            Name NVARCHAR(32) NOT NULL,
            Floor NVARCHAR(8) NOT NULL,
            State NVARCHAR(10) NOT NULL,
			
            UNIQUE
            (
                GameID ASC,
                Name ASC
            )
        );
        '''
        # TODO: Check all the lenghts of the NVARCHAR's to make sure they are the correct lengths.
    cursor.execute(query)
    conn.commit()
    cursor.close()


# Drops the Tile table.
def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Betrayal.Tile;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()
    

# Inserts one Tile and returns that TileID.
def insert_one(conn, row):
    cursor = conn.cursor()
    tile_id = -1
    if row:
        query = f'''
            INSERT INTO Betrayal.Tile VALUES {row};
            '''
        cursor.execute(query)
        conn.commit()
        tile_id = cursor.lastrowid
    else:
        print('ERROR: Cannot set default values for table Tile. Must give foreign key.')
    cursor.close()
    return tile_id


# Inserts many Tiles into Tile table.
def insert_many(conn, rows):
    cursor = conn.cursor()
    if rows:
        cursor.executemany('''INSERT INTO Betrayal.Tile VALUES (%d, %s, %s, %s)''', rows)
        conn.commit()
    else:
        print('ERROR: You must provide row values for the insert_many method! Can not be left to default!')
    cursor.close()


# Gets one row given a tile_id.
def get_one(conn, tile_id):
    cursor = conn.cursor()
    query = f'''
        SELECT * 
        FROM Betrayal.Tile T
        WHERE T.TileID = {tile_id};
        '''
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    return row


# Gets all the rows from Tile table.
def get_all(conn, conditional):
    cursor = conn.cursor()
    query = f'''
        SELECT *
        FROM Betrayal.Tile
        {conditional};
        '''
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


# Gets the column names for the Tile table.
def get_column_names():
    return ['TileID', 'GameID', 'Name', 'Floor', 'State']


# Updates an element for a specific Tile
# the 'setter' parameter will be a string Example: "State = N'Played'"
def update(conn, tile_id, setter):
    cursor = conn.cursor()
    query = f'''
        UPDATE Betrayal.Tile
        SET {setter}
        WHERE TileID = tile_id
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()
