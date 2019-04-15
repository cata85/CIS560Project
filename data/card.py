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
