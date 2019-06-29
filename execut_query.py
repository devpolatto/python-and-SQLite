import sqlite3
from bd.skill import insert


conn = sqlite3.connect('base.bd')
pointer = conn.cursor()


query = insert('arcanjo', '99766539', 'arcanjo@gmail')




pointer.execute()
conn.commit()
conn.close()