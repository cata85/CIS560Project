import pymssql


def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Game')
        CREATE TABLE Betrayal.Game
        (
            GameID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            StartDate DATETIMEOFFSET NOT NULL DEFAULT(SYSDATETIMEOFFSET())
        );
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()


def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Betrayal.Game;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()

