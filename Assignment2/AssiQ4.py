statelist=["Delhi","Bihar","Goa","Gujarat","Assam"]
vowel=["a","e","i","o","u","A","E","I","O","U"]
for items in statelist:
    if items[len(items)//2] in vowel:
        print(items[len(items)//2],end="")