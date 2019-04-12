import pymssql


def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Character')
        CREATE TABLE Character
        (
            CharacterID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            PlayerID INT NOT NULL FOREIGN KEY
                REFERENCES Player(PlayerID),
            CharacterName NVARCHAR(32) NOT NULL,
            TileID INT NOT NULL FOREIGN KEY
                REFERENCES Tile(TileID),
            Speed INT NOT NULL,
            Strength INT NOT NULL,
            Sanity INT NOT NULL,
            Intelligence INT NOT NULL,
            Birthday DATETIMEOFFSET NOT NULL,

            UNIQUE
            (
                PlayerID ASC,
                CharacterName ASC
            )
        );
        ''' 
        # TODO: IS TILEID A FOREIGN KEY?
    cursor.execute(query)
    conn.commit()
    cursor.close()


def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Character;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()