Countries=["Finland","Germany","Sweden","Ireland","Turkey"]
list1=[]

for li in Countries:
   if li.find("and")!=-1:
       list1.append(li)

print(list1)