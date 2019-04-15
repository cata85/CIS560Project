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
