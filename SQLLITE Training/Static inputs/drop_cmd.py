import sqlite3
'Bootcamp2023.db'
conn=sqlite3.connect('../Bootcamp2023.db')
print(conn)

querry="drop table participants"
conn.execute(querry)
conn.commit()