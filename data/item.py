import pymssql


def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Item')
        CREATE TABLE Item
        (
            ItemID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            TileID INT NOT NULL FOREIGN KEY
                REFERENCES Tile(TileID),
            CharacterID INT NOT NULL FOREIGN KEY
                REFERENCES Character(CharacterID),
            Name NVARCHAR(32) NOT NULL,

            UNIQUE
            (
                TileID ASC,
                CharacterID ASC
            )
        );
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()


def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Item;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()

