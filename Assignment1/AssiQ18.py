#matrix

matrix1=[[1,2,3],
         [4,5,6],
         [7,8,9]]

matrix2=[[10,11,12],
         [13,14,15],
         [16,17,18]]

#Iterate matrix

for row in matrix1:
    print(row)

for row in matrix2:
    print(row)

result= [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

print("Addition of matrix")
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j]=matrix1[i][j]+matrix2[i][j]

for row in result:
    print(row)

print("Subtraction of matrix")
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j]=matrix1[i][j]-matrix2[i][j]

for row in result:
    print(row)
