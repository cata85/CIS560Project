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
                PlayerID ASC
            )
        );
        ''' 
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


# Inserts one Character and returns that CharacterID.
def insert_one(conn, row, game_id):
    cursor = conn.cursor()
    character_id = -1
    if row:
        try:
            row = (str(row[1]), str(row[2]), str(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]))
        except:
            return character_id
        query = f'''
            INSERT Betrayal.Character(PlayerID, CharacterName, TileID, Speed, Might, Sanity, Knowledge)
            SELECT P.PlayerID, V.CharacterName, T.TileID, V.Speed, V.Might, V.Sanity, V.Knowledge
            FROM (VALUES {row}) AS V(PlayerName, CharacterName, TileName, Speed, Might, Sanity, Knowledge)
                INNER JOIN Betrayal.Player P ON P.PlayerName = V.PlayerName
                INNER JOIN Betrayal.Tile T ON T.TileName = V.TileName
            WHERE P.GameID = {game_id}
                AND T.GameID = {game_id};
            '''
        try:
            cursor.execute(query)
            conn.commit()
            character_id = cursor.lastrowid
        except:
            cursor.close()
            return character_id
    else:
        print('ERROR: Cannot set default values for table Character. Must give foreign key.')
    cursor.close()
    return character_id


# Inserts many Characters into Character table.
def insert_many(conn, rows):
    cursor = conn.cursor()
    if rows:
        cursor.executemany('''INSERT INTO Betrayal.Character VALUES (%d, %s, %d, %d, %d, %d, %d)''', rows)
        conn.commit()
    else:
        print('ERROR: You must provide row values for the insert_many method! Can not be left to default!')
    cursor.close()


# Gets one row given a character_id.
def get_one(conn, character_id):
    cursor = conn.cursor()
    query = f'''
        SELECT * 
        FROM Betrayal.Character C
        WHERE C.CharacterID = {character_id};
        '''
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    return row


# Gets all the rows from Character table.
def get_all(conn, game_id):
    cursor = conn.cursor()
    query = f'''
        SELECT C.CharacterID, P.PlayerName, C.CharacterName, T.TileName, C.Speed, C.Might, C.Sanity, C.Knowledge
        FROM Betrayal.Character C
            INNER JOIN Betrayal.Player P ON P.PlayerID = C.PlayerID
            INNER JOIN Betrayal.Tile T  ON C.TileID = T.TileID
        WHERE P.GameID = {game_id};
        '''
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


# Gets the column names for the Character table.
def get_column_names():
    return ['CharacterID', 'PlayerName', 'CharacterName', 'TileName', 'Speed', 'Might', 'Sanity', 'Knowledge']


# Updates an element for a specific CharacterID
def update(conn, row):
    cursor = conn.cursor()
    character_id = -1
    if row:
        try:
            row = (int(row[1]), str(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]))

    query = f'''
        UPDATE Betrayal.Character
        SET 
            TileID = T.TileID,
            Speed = {row[3]},
            Might = {row[4]},
            Sanity = {row[5]},
            Knowledge = {row[6]}
        FROM Betrayal.Tile T
            INNER JOIN Betrayal.Monster M ON T.TileID = M.TileID
        WHERE C.CharacterID = {row[1]} AND T.TileName = {row[2]}
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()