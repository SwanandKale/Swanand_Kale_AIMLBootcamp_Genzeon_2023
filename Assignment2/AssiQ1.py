#way1
"""str1=input("Enter the string ").split(",")
set1=set(str1)
li=list(set1)
li.sort()
print(li)"""

#way2
str1=input("Enter the string")
str2=str1.split(",")
count1=len(str2)
print(count1)

for x in range(count1):
    str2.sort()

set1=set(str2)
print(set1,type(set1))