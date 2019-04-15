import pymssql


# Creates the Item table.
def create_table(conn):
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Item')
        CREATE TABLE Betrayal.Item
        (
            ItemID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
            TileID INT NOT NULL FOREIGN KEY
                REFERENCES Betrayal.Tile(TileID),
            Name NVARCHAR(32) NOT NULL
        );
        '''
    cursor.execute(query)
    conn.commit()
    cursor.close()


# Drops the Item table.
def drop_table(conn):
    cursor = conn.cursor()
    query = '''DROP TABLE IF EXISTS Betrayal.Item;'''
    cursor.execute(query)
    conn.commit()
    cursor.close()


# Inserts one Item and returns that ItemID.
def insert_one(conn, row):
    cursor = conn.cursor()
    item_id = -1
    if row:
        query = f'''
            INSERT INTO Betrayal.Item VALUES {row};
            '''
        cursor.execute(query)
        conn.commit()
        item_id = cursor.lastrowid
    else:
        print('ERROR: Cannot set default values for table Item. Must give foreign key.')
    cursor.close()
    return item_id


# Inserts many Items into Item table.
def insert_many(conn, rows):
    cursor = conn.cursor()
    if rows:
        cursor.executemany('''INSERT INTO Betrayal.Item VALUES (%d, %s)''', rows)
        conn.commit()
    else:
        print('ERROR: You must provide row values for the insert_many method! Can not be left to default!')
    cursor.close()
