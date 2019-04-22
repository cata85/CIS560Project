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
    

# Inserts one Player and returns that PlayerID.
def insert_one(conn, row):
    cursor = conn.cursor()
    player_id = -1
    if row:
        query = f'''
            INSERT INTO Betrayal.Player VALUES (%d, %s)
            '''
        cursor.execute(query, row)
        conn.commit()
        player_id = cursor.lastrowid
    else:
        print('ERROR: Cannot set default values for table Player. Must give foreign key and name.')
    cursor.close()
    return player_id


# Inserts many Players into Player table.
def insert_many(conn, rows):
    cursor = conn.cursor()
    if rows:
        cursor.executemany('''INSERT INTO Betrayal.Player VALUES (%d, %s)''', rows)
        conn.commit()
    else:
        print('ERROR: You must provide row values for the insert_many method! Can not be left to default!')
    cursor.close()


# Gets one row given a player_id.
def get_one(conn, player_id):
    cursor = conn.cursor()
    query = f'''
        SELECT * 
        FROM Betrayal.Player P
        WHERE P.PlayerID = {player_id};
        '''
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    return row


# Gets all the rows from Player table.
def get_all(conn, game_id):
    cursor = conn.cursor()
    query = f'''
        SELECT P.PlayerID, P.PlayerName
        FROM Betrayal.Player P
        WHERE P.GameID = {game_id};
        '''
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


# Gets the column names for the Player table.
def get_column_names():
    return ['PlayerID', 'PlayerName']
