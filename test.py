import config
import pymssql


conn = pymssql.connect(
    server=config.SERVER, 
    user=config.USER, 
    password=config.PASSWORD, 
    database=config.DB
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
data = cursor.fetchall()
for row in data:
    print(row)

cursor.execute("SELECT * FROM Betrayal.Game;")
data = cursor.fetchall()
for row in data:
    print(row)
    