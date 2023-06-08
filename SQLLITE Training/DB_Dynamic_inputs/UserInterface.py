from Main_App.Input_pack import user_inputs as u
from Main_App.Operations_Pack import fetch_records as f
from Main_App.Operations_Pack import fetch_Branch as fb
from Main_App.Operations_Pack import update_record as ub
while True:
    print("----------------MENU-------------------")
    print('''
    1. Enter Participants Details
    2. Fetch the participants Details
    3. Fetch participnts based on branch
    4. update wrongly enter name change
    5.exit
    ''')
    print("Choose any option from above menu : ")
    ch=int(input())
    if ch==1:
        u.input_data()
    elif ch==2:
        f.display()
    elif ch==3:
        inp_branch=input("Enter the branch :: ")
        fb.fetch_branch(inp_branch)
    elif ch==4:
        str=input("Enter the id and Name")
        id,name=str.split(',')
        print(id,name)
        ub.update_method(int(id),name)
    elif ch==5:
        break


