import pymssql


def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Monster')
        CREATE TABLE Betrayal.Monster
        (
            MonsterID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            TileID INT NOT NULL FOREIGN KEY
                REFERENCES Betrayal.Tile(TileID),
            Name NVARCHAR(32) NOT NULL
        );
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()


def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Betrayal.Monster;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()