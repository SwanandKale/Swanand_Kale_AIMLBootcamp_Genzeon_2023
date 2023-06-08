str="This program converts spaces into hyphen"
str2=""

for c in str:
    if c!=" ":
        str2=str2+c
    else:
        str2=str2+"-"

print(str2)
