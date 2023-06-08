from functools import reduce
input=[25,12,33,12,8,10]

sum=reduce(lambda x,y :x+y,input)
print(sum)