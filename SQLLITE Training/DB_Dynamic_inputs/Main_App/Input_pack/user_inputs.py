import sqlite3
'Bootcamp2023.db'
conn=sqlite3.connect('../Bootcamp2023.db')
print(conn)

def input_data():
    data={}
    g_id=int(input("Enter G_id"))
    name=input("Enter name")
    branch=input("Enter Branch ::")
    study=input("Enter study:: ")
    data["g_id"]=g_id
    data["name"]=name
    data["branch"]=branch
    data["study"]=study

    conn.execute('''
    insert into participants (G_id,name,branch,study) values(?,?,?,?)
    ''',(data.get('g_id'),data.get('name'),data.get('branch'),data.get('study')))
    conn.commit()

    print("Data entered successfully")
    conn.close()
