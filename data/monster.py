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
            MonsterName NVARCHAR(32) NOT NULL
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
def insert_one(conn, row, game_id):
    cursor = conn.cursor()
    monster_id = -1
    if row:
        row = (row[1], row[2])
        query = f'''
            INSERT Betrayal.Monster(TileID, MonsterName)
            SELECT T.TileID, V.MonsterName
            FROM (VALUES {row}) AS V(TileName, MonsterName)
                INNER JOIN Betrayal.Tile T ON T.TileName = V.TileName
            WHERE T.GameID = {game_id};
            '''
        try:
            cursor.execute(query)
            conn.commit()
            monster_id = cursor.lastrowid
        except:
            cursor.close()
            return monster_id
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


# Gets one row given a monster_id.
def get_one(conn, monster_id):
    cursor = conn.cursor()
    query = f'''
        SELECT * 
        FROM Betrayal.Monster M
        WHERE M.MonsterID = {monster_id};
        '''
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    return row


# Gets all the rows from Monster table.
def get_all(conn, game_id):
    cursor = conn.cursor()
    query = f'''
        SELECT M.MonsterID, T.TileName, M.MonsterName
        FROM Betrayal.Monster M
            INNER JOIN Betrayal.Tile T ON T.TileID = M.TileID
        WHERE T.GameID = {game_id};
        '''
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


# Gets the column names for the Monster table.
def get_column_names():
    return ['MonsterID', 'TileID', 'MonsterName']


# Updates an element for a specific Monster
# the 'setter' parameter will be a string Example: "TileID = 14"
def update(conn, row):
    cursor = conn.cursor()
    monster_id = -1
    if row:
        try:
            row = (int(row[1]), str(row[2]))
        except:
            return monster_id
        query = f'''
            UPDATE Betrayal.Monster
            SET TileID = T.TileID
            FROM Betrayal.Tile T
                INNER JOIN Betrayal.Monster M ON T.TileID = M.TileID
            WHERE I.ItemID = {row[1]} AND T.TileName = {row[2]}
            '''
        try:
            cursor.execute(query)
            conn.commit()
            monster_id = cursor.lastrowid
        except:
            cursor.close
            return monster_id
    else:
        print('ERROR: Input data incorrect')
    cursor.close()
    return monster_id
