file1=open("Bill.txt","w")
file1.write(input("Enter the bill"))
file1.close()

class InvalidProductBillException(Exception):
    pass
file1=open("Bill.txt",'r')
ans=file1.read()
try:
    if(ans<'0'):
        raise InvalidProductBillException
    else:
        print("You need to pay amount",ans)
except InvalidProductBillException as ie:
    print("Exception occured",ie)

file1.close()