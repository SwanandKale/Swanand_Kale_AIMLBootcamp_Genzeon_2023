import sqlite3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)

'''
insert into tablename values('','')
'''
conn.execute('''
insert into participants values(101,'Swanand','Mech','Btech','kaleswanand280101@gmail.com')
''')
conn.commit()

