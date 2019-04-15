import config
import pymssql


conn = pymssql.connect(
    server=config.SERVER, 
    user=config.USER, 
    password=config.PASSWORD, 
    database=config.DB
)
cursor = conn.cursor()

print('TABLES:')
cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
data = cursor.fetchall()
for row in data:
    print(row)

print('\nGAMES:')
cursor.execute("SELECT * FROM Betrayal.Game;")
data = cursor.fetchall()
for row in data:
    print(row)

print('\nCARDS:')
cursor.execute("SELECT * FROM Betrayal.Card;")
data = cursor.fetchall()
for row in data:
    print(row)

print('\nPLAYERS:')
cursor.execute("SELECT * FROM Betrayal.Player;")
data = cursor.fetchall()
for row in data:
    print(row)
    
print('\nTILES:')
cursor.execute("SELECT * FROM Betrayal.Tile;")
data = cursor.fetchall()
for row in data:
    print(row)

print('\nCHARACTERS:')
cursor.execute("SELECT * FROM Betrayal.Character;")
data = cursor.fetchall()
for row in data:
    print(row)

print('\nMONSTERS:')
cursor.execute("SELECT * FROM Betrayal.Monster;")
data = cursor.fetchall()
for row in data:
    print(row)

print('\nITEMS:')
cursor.execute("SELECT * FROM Betrayal.Item;")
data = cursor.fetchall()
for row in data:
    print(row)
