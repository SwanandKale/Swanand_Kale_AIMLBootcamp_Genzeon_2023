#all string methods return new values , they do not change original string
str1="swaaanand"
str2="SWANAND"
print(str1.capitalize()) #first letter capital
print(str2.casefold()) #string lowercase
print(str2.center(10))

print(str1.count(str1[2]))
print(str1.encode())
print(str1.find("a"))#Returned the position of where it was found
print(str1.endswith("d"))
print(str1.index("a"))#Returned the position of where it was found

str3="1234"
print(str3.isdigit())
print(str2.isdigit())
print(str3.isalpha())

print(str3.rfind("2"))#Searches the string for a specified value and returns the last position of where it was found

