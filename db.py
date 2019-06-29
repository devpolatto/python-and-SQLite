import sqlite3

#connection bd
con = sqlite3.connect('base.db')
#manipulador
cur = con.cursor()

query = '''
    CREATE TABLE users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    );
    
'''

cur.execute(query)
con.commit()
con.close()