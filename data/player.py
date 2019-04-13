import pymssql


# Creates the Player table.
def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Player')
        CREATE TABLE Betrayal.Player
        (
            PlayerID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            GameID INT NOT NULL FOREIGN KEY
                REFERENCES Betrayal.Game(GameID),
            PlayerName NVARCHAR(32) NOT NULL,

            UNIQUE
            (
                GameID ASC,
                PlayerName ASC
            )
        );
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()


# Drops the Player table.
def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Betrayal.Player;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()
    