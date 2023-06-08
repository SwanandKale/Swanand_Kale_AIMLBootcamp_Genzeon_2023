"""x = float(input("Enter Number :: "))

decimal = int(x)
binary = bin(int(x))
hexa = hex(int(x))
octa = oct(int(x))

print("Decimal :: ",decimal)
print("Binary :: ",binary)
print("HexaDecimal :: ",hexa)
print("OctaDecimal :: ",octa)"""

def add(a,b,c):
    return a+b+c
print(add(10,20,30))

def A(a,b=1,c=2):
    return a+b+c
print(A(10,12))

def inc(num):
    return num+2

li=[1,2,3,4]
res_list=list(map(inc,li))
print(res_list)

print("-----------------------------------------")
inp=int(input("Enter thr num : "))
def eor(num):
    if num%2==0:
        return "even number",num
    else:
        return "it is not even no ",num

print(eor(inp))
