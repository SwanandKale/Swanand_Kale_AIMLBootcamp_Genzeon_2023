import sqlite3
'Bootcamp2023.db'
conn=sqlite3.connect('../Bootcamp2023.db')
print(conn)

querry='delete from participants where g_id=101'

conn.execute(querry)
conn.commit()