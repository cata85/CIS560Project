import pymssql


def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Tile')
        CREATE TABLE Tile
        (
            TileID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            GameID INT NOT NULL FOREIGN KEY
                REFERENCES Game(GameID),
            Name NVARCHAR(32) NOT NULL,
            Floor NVARCHAR(1) NOT NULL,
            State NVARCHAR(1) NOT NULL,
            Text NVARCHAR(128) NOT NULL

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


def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Tile;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()