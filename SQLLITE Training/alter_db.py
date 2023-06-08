import sqlite3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)

'''
Renamecolumns
add a column
change datatype
remove / add any constriant
'''

'''
add column - maildId
ALTER table table_name add column column_name datatype constriants
'''

conn.execute('''
alter table participants add column email_id text not null
''')