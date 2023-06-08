import sqlite3
'Bootcamp2023.db'
conn=sqlite3.connect('../Bootcamp2023.db')
print(conn)

details = conn.execute('select * from participants')

for x in details:
    print(x)