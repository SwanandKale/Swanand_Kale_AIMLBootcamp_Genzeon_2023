
def counting_nos(input1):
    count=0
    while input1!=0:
        input1=int(input1/10)
        count=count+1
    return count

input1 = int(input("Enter the Number :: "))
file1=open("AssignmentResult.txt",'w')
file1.write(str(counting_nos(input1)))
print("Output saved in file")


