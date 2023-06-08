tup0=(1,3,4,5,2)
tup1=("hi",2,3.4)
tup2=("hello",tup1,tup0)
print(tup0);
print(tup2[1][0]);

#slicing nested tuples
print(tup2[0][1:3])

print(tup0.count(1))
print(max(tup0))
print(min(tup0))
print(len(tup0))

print("------------------------")
#sets
s1={1,3}
s2={1,2,3,"hi",(1,2,3,4)}

l=[1,3,5,7]
s3=set(l)
print(s3)

s1.add(2)
print(s1)
s1.update([2,3,4])
print(s1)

s1.discard(5)
print(s1)

s1.remove(2)
print(s1)

a={1,2,3,4}
b={4,5,6,7}

print("Union")
print(a|b)#union
print(a.union(b))

print(a.intersection(b))#intersection
print(a&b)

#difference
print("Difference");
print(a-b)
print(b-a)

print("Dictonary")
dic={"name":"swanand","phone":"7887522695","Address":"Satara"}
print(dic)
print(dic.keys())
print(dic.values())