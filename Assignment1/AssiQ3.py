#Tuples are ordered but immutable and written in round bracket
tup1=("Satara","Pune","Kohlapur")
print(type(tup1),tup1)

print("welcome to python training program"[3:10][::-1])

print("A series of characters designated as one object known as a string"[::-1][4::3])

str1="was it a car or cat I saw"
print(str1[::-1].upper())

x=int(input("Enter value of x"))
y=2*x
str2=""

for loop in range(x):
    str2=str2+"z"

for loop1 in range(y):
    str2=str2+"o"

print(str2)