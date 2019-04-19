import pymssql


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
            Name NVARCHAR(32) NOT NULL,
            Type NVARCHAR(5) NOT NULL,
            State NVARCHAR(10) NOT NULL DEFAULT(N'Not Played'),

            UNIQUE
            (
                GameID ASC,
                Name ASC
            )
        );
        '''
		
		# TODO: Check all the lenghts of the NVARCHAR's to make sure they are the correct lengths.
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
def insert_one(conn, row):
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
def get_all(conn, conditional):
    cursor = conn.cursor()
    query = f'''
        SELECT *
        FROM Betrayal.Card
        {conditional};
        '''
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


# Gets the column names for the Card table.
def get_column_names():
    return ['CardID', 'GameID', 'Name', 'Type', 'State']


# Updates an element for a specific Card
# the 'setter' parameter will be a string Example: "State = N'Played'"
def update(conn, card_id, setter):
    cursor = conn.cursor()
    query = f'''
        UPDATE Betrayal.Card
        SET {setter}
        WHERE CardID = card_id
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()
