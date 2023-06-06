"""a=int(input("Enter a num")) #its like scanf
print(a)"""

"""b=input("Enter num")
print(b,type(b))# it is string"""

#format
print("{} are learning {} programming at {}".format("traniees","python","Genzeon"));

#placeholder
print("%s world"%("Hello"))

print("---------------Decision Making--------------")

#if statement
var=10
if var>10:
    print("true")
    print(var)
else:
    print("False")
    print(var)

#nested ifelse

"""age=int(input("Enter age"))
if age<20:
    print("50 % discount applied")
elif (age>20 and age<45):
    print("20 % discount")
elif age>45 and age<60:
    print("40 % discount")
else:
    print("60% discount")"""

print("--------------Loops --------------")

#for loop
ln=[23,43,46,77,87,67]
sum=0

for val in ln:
    sum=sum+val
print(sum)

for i in range(1,11,2):
    print(i)

for i in range(65,91):
    print(chr(i))

print("----------BREAK------------")