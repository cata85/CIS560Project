import pymssql


def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Player')
        CREATE TABLE Player
        (
            PlayerID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            GameID INT NOT NULL FOREIGN KEY
                REFERENCES Game(GameID),
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


def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Player;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()