#Data types in python

#Integer
x=5
print(type(x))

#str
x='5'
print(type(x))

#bool
x=True
print(type(x))

#float
x=5.3
print(type(x))

#list
x=[28,"Swanand",25.4]
print(type(x))

#tuple
x=(28,"Swanand",25.9)
print(type(x))

#dict
x={28:"Swanand",29:"kale"}
print(type(x))

#set
x={28,28,29,37}
print(x)
print(type(x))

#Assigning multiple values

name,age,marks="Santos",36,56.5;

print(name,type(name))
print(age,type(age))
print(marks,type(marks))

#One value to multiple variables

var1=var2=var3="assigning multiple values"
print(var2,type(var2))

#Unpack a collection

list1=[28,"Swanand","Rahul",78.5]
date,name1,name2,weight=list1
print(date,name1,name2,weight)

#Combinitions

#print("Swanand"+"2.5") dosent work in py
print(5/3) #automatically converts into float

'''
text type= str
numeric type=int , float , complex
sequence type=list,tuple,range
mapping type=dict
set type=set, frozenset
boolean type=bool
binary types=bytes,bytearray,memoryview
none type=Nonetype
'''

x=76767677676767676767676
print(x,type(x))

