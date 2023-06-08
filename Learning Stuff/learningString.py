#Multiline strings

a="""swanand
kale"""
print(a)

string1="Amit rohra"
print(string1[0])

#java forEach loop
for x in "banana":
    print(x)

#len
str="Swanand kale"
print(len(str))

#to check certain phrase or word in string we use (in keyword)
print("kale" in str)

#if-in combination
if "Swanand" in str:
    print("Present")

str1="It's not about ideas , it's about making ideas happen"
print("about" not in str1)

#if-Not combi
if "swanand" not in str1:
    print("swanand is not present in str1")

print("--------------------------------------------------------")
print("slicing Operation")
str2="   Swanand kale   "
print(str2[:4]) #slice from start
print(str2[2:]) #slice from end

print(str2[-3:-1])
print(str2[0:-1])

print(str2.upper())
print(str2.lower())

print(str2.strip()) #just trim the starting and ending white spaces

print(str2.replace("S","Ch")) #replace operation

str3="world trade center"
print(str3.split(" "))
print(str3.split(" ")[2][0:2])

#Concate strings
str4="penguin"
str5="piyush{}" #-> {} it is placeholder
print(str4+" "+str5)

#Can concat String and Integer using concat
x=7
print(str5.format(x))

name="My Name is \"Swanand\" kale"
print(name)
