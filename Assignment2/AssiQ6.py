statelist=["Delhi","Bihar","UP","Goa","Gujarat","Assam","AP"]
str=""
vowel=["a","e","i","o","u","A","E","I","O","U"]
for list in statelist:
    if list[-2] in vowel:
        str=str+list[-2]

print(str[::-1].upper())