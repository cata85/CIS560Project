import pymssql
import _mssql


# Creates the Card table.
def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Card')
        CREATE TABLE Betrayal.Card
        (
            CardID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            GameID INT NOT NULL FOREIGN KEY
                REFERENCES Betrayal.Game(GameID),
            CardName NVARCHAR(32) NOT NULL,
            Type NVARCHAR(5) NOT NULL,
            State NVARCHAR(10) NOT NULL DEFAULT(N'Not Played'),

            UNIQUE
            (
                GameID ASC,
                CardName ASC
            )
        );
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()


# Drops the Card table.
def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Betrayal.Card;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()


# Inserts one Card and returns that CardID.
def insert_one(conn, row, game_id):
    cursor = conn.cursor()
    card_id = -1
    if row:
        query = f'''
            INSERT INTO Betrayal.Card VALUES {row};
            '''
        cursor.execute(query)
        conn.commit()
        card_id = cursor.lastrowid
    else:
        print('ERROR: Cannot set default values for table Card. Must give foreign key.')
    cursor.close()
    return card_id


# Inserts many Cards into Card table.
def insert_many(conn, rows):
    cursor = conn.cursor()
    if rows:
        cursor.executemany('''INSERT INTO Betrayal.Card VALUES (%d, %s, %s, %s)''', rows)
        conn.commit()
    else:
        print('ERROR: You must provide row values for the insert_many method! Can not be left to default!')
    cursor.close()


# Gets one row given a card_id.
def get_one(conn, card_id):
    cursor = conn.cursor()
    query = f'''
        SELECT * 
        FROM Betrayal.Card C
        WHERE C.CardID = {card_id};
        '''
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    return row


# Gets all the rows from Card table.
def get_all(conn, game_id):
    cursor = conn.cursor()
    query = f'''
        SELECT C.CardID, C.CardName, C.Type, C.State
        FROM Betrayal.Card C
        WHERE C.GameID = {game_id};
        '''
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


# Gets the column names for the Card table.
def get_column_names():
    return ['CardID', 'CardName', 'Type', 'State']


# Updates an element for a specific Card
# the 'setter' parameter will be a string Example: "State = N'Played'"
def update(conn, row):
    cursor = conn.cursor()
    card_id = -1
    if row:
        try:
            row = (str(row[0]), str(row[1]))
        except:
            return card_id
        query = f'''
            UPDATE Betrayal.Card
            SET State = N'{row[1]}'
            WHERE CardID = N'{row[0]}'
            '''
        try:
            print(query)
            cursor.execute(query)
            conn.commit()
            card_id = cursor.lastrowid
        except _mssql.MSSQLDatabaseException as e:
            print(e)
            cursor.close
            return card_id
    else:
        print('ERROR: Input data incorrect')
    cursor.close()
    return card_id