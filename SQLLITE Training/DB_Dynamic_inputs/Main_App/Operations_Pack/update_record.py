import sqlite3
'Bootcamp2023.db'
conn=sqlite3.connect('../Bootcamp2023.db')
print(conn)

def update_method(id,str1):
    conn.execute("update participants set name='"+str1+"' where g_id='"+str(id)+"'")
    conn.commit()