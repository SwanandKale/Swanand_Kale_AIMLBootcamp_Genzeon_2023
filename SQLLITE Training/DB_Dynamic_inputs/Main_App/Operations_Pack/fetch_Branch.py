import sqlite3
'Bootcamp2023.db'
conn=sqlite3.connect('../Bootcamp2023.db')
print(conn)

def fetch_branch(inp_branch):
    conn.execute("select * from participants where branch='"+str(inp_branch)+"'")