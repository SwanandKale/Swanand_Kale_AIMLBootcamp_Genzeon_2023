import sqlite3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)

'''
describe tablename -> sql
pragma table_info(tablename) -> sqlite
'''

details=conn.execute("pragma table_info(participants)")
print(details)

#to traverse the data because details is now cursor object
for i in details:
    print(i)