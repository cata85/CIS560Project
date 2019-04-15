import pymssql


# Creates the Monster table.
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


# Drops the Monster table.
def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Betrayal.Monster;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()
    

# Inserts one Monster and returns that MonsterID.
def insert_one(conn, row):
    cursor = conn.cursor()
    monster_id = -1
    if row:
        query = f'''
            INSERT INTO Betrayal.Monster VALUES {row};
            '''
        cursor.execute(query)
        conn.commit()
        monster_id = cursor.lastrowid
    else:
        print('ERROR: Cannot set default values for table Monster. Must give foreign key.')
    cursor.close()
    return monster_id


# Inserts many Monsters into Monster table.
def insert_many(conn, rows):
    cursor = conn.cursor()
    if rows:
        cursor.executemany('''INSERT INTO Betrayal.Monster VALUES (%d, %s)''', rows)
        conn.commit()
    else:
        print('ERROR: You must provide row values for the insert_many method! Can not be left to default!')
    cursor.close()
