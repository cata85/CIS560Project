import pymssql


# Creates the Game table.
def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Game')
        CREATE TABLE Betrayal.Game
        (
            GameID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            StartDate DATETIMEOFFSET NOT NULL DEFAULT(SYSDATETIMEOFFSET()),
			Haunt INT NOT NULL DEFAULT(0),
			TrackValue INT NOT NULL DEFAULT(0)
        );
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()


# Drops the Game table.
def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Betrayal.Game;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()


# Inserts one Game and returns that GameID.
def insert_one(conn, row=''):
    cursor = conn.cursor()
    query = '''INSERT INTO Betrayal.Game DEFAULT VALUES;'''
    cursor.execute(query)
    conn.commit()
    game_id = cursor.lastrowid
    cursor.close()
    return game_id
