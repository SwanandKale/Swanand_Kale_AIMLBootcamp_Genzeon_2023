"""
list are ordered , mutable(can modify elements),allow duplicates
"""

list1=["Genzeon","World Trade center","Eon Park","Irani Cafe"]
print(list1)

#list constructor
mylist=list(("swanand","kale"))
print(mylist)

# 1.len()
print(len(list1),type(list1))

# 2.assceing by index (+ve and -ve)
print(list1[2])

# 3.range
print(list1[1:3])

# changing list items
list1[0]="keshavnagar"
print(list1)

list1[4:5]=["karvenagar","Kondhwa","ISKON"]
print(list1,len(list1))

#Inserting values
list1.insert(0,"Pune")
print(list1)

#appending and extending
list1.append("Satara")
print(list1)
list2=["Raigad","Torana","Ajinkyatara"]

list1.extend(list2)
print(list1)

#you can add any iterable using .extend()
tup1={"oranges","kiwis"}
list1.extend(tup1)
print(list1)

#remove() from list
list1.remove(list1[0])
print(list1)
list1.pop(1)
print(list1)

#printing
print("--------Priting list using LOOPS---------")
list3=["Oranges","Mangoes","Bananas"]

for x in list3:
    print(x)

print("printing using for loop")
for i in range(len(list3)):
    print(list3[i])

print("printing using While loop")
x=0
while x<len(list3):
    print(list3[x])
    x=x+1

#Sorting
print("Sort the list -> for descending .sort(reverse=true)")
list3.sort(reverse=True)
print(list3)

#Copying
print("Copying list3 to mylist")
mylist1=list3.copy()
print(mylist1)

print("Another way to copy list(list3)-> constructor")
mylist2=list(list3)
print(mylist2)
