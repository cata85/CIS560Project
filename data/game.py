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
			Haunt INT NULL DEFAULT(NULL),
			TrackValue INT NULL DEFAULT(NULL)
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
def insert_one(conn, row):
    cursor = conn.cursor()
    if row:
        query = f'''
            INSERT INTO Betrayal.Game VALUES {row};
            '''
    else:
        query = '''INSERT INTO Betrayal.Game DEFAULT VALUES;'''
    cursor.execute(query)
    conn.commit()
    game_id = cursor.lastrowid
    cursor.close()
    return game_id


# Inserts many Games into Game table.
def insert_many(conn, rows):
    cursor = conn.cursor()
    if rows:
        cursor.executemany('''INSERT INTO Betrayal.Game VALUES (%s, %d, %d)''', rows)
        conn.commit()
    else:
        print('ERROR: You must provide row values for the insert_many method! Can not be left to default!')
    cursor.close()


# Gets one row given a game_id.
def get_one(conn, game_id):
    cursor = conn.cursor()
    query = f'''
        SELECT * 
        FROM Betrayal.Game G
        WHERE G.GameID = {game_id};
        '''
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    return row


# Gets all the rows from Game table.
def get_all(conn, game_id):
    cursor = conn.cursor()
    query = f'''
        SELECT *
        FROM Betrayal.Game G
        WHERE G.GameID = {game_id};
        '''
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


# Gets the column names for the Game table.
def get_column_names():
    return ['GameID', 'StartDate', 'Haunt', 'TrackValue']


# Updates an element for a specific Game
# the 'setter' parameter will be a string Example: "HauntID = 23"
def update(conn, game_id, setter):
    cursor = conn.cursor()
    query = f'''
        UPDATE Betrayal.Game
        SET {setter}
        WHERE GameID = {game_id}
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()
