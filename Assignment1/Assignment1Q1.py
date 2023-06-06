#String methods Example
#1. convert first character to uppercase : capitalize()
name="swanand";
print(name.capitalize())

#2.convert string to lowercase : casefold()
str="SWANAND"
print(str.casefold())

#3. returns no of times specified value occurs in string : count()
name1="swanand kale"
print(name1.count("a"))

#4 endswith() : return true if string ends with specified value
name2="Akash phule"
print(name2.endswith("le"))

#5 find() : searches string for a specified value and returns the position where it found : index()
name3="Nitish rana"
print(name3.find("i"))

#6. format() : formats the specified value and insert them inside the string's placeholder
name4="Swanand {}".format("kale")
print("name 4 "+name4)

#7. isalnum() : returs true if all characters in strings are alphanumeric(a-z A-Z 0-9)
name5="123S"
print(name5.isalnum())

#8 isalpha() : returns true if all characters i the string are alphabet
name6="k3shav"
print(name6.isalpha())

#9 isdigit() : returs true for 0-9
name7="5556"
print(name7.isdigit())

#10. join() : takes all items in an iterable and joins them into one string
tup1={"swanand","shubham","Rahul"}
delimiter="#"
print(delimiter.join(tup1))

#11 strip() : trim left and right whitespaces
space1="  swanand  kale  "
print(space1.strip())
print(space1.rstrip())

#12 split() : split the string and give list as op
str2="swanand,kale"
print(str2.split(","))
