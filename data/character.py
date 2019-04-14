import pymssql


# Creates the Character table.
def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Character')
        CREATE TABLE Betrayal.Character
        (
            CharacterID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            PlayerID INT NOT NULL FOREIGN KEY
                REFERENCES Betrayal.Player(PlayerID),
            CharacterName NVARCHAR(32) NOT NULL,
            TileID INT NOT NULL FOREIGN KEY
                REFERENCES Betrayal.Tile(TileID),
            Speed INT NOT NULL,
            Might INT NOT NULL,
            Sanity INT NOT NULL,
            Knowledge INT NOT NULL,

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


# Drops the Character table.
def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Betrayal.Character;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()
