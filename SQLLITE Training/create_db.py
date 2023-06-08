#steps
"""
1.importing sqllite3
2.create a database
3.establishconnection with db
4. creating table in db -> write a query
5. execute the query
"""

import sqlite3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)

#create a table
query='''
create table participants(g_id int primary key , name text not null, branch text not null,study text not null DEFAULT 'Btech')
'''
conn.execute(query)