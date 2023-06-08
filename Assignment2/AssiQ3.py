statelist=["Delhi","Telananga","Goa","AP","Kerala"]
str=""
for list in statelist:
    str=str+list[0].lower()
    str=str+(list[len(list)-1].upper())

print(str)