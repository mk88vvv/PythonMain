n = 9
matrix = []
row = []
a = '.'
b = '*'
for i in range(n):
    row.append(a)
for i in range(n):
    matrix.append(row.copy())
for i in range(len(matrix)//2, n+4):#horizont
    matrix[len(matrix)//2][i-4]=b
for i in range(len(matrix)//2, n+4):#vert
    matrix[i-4][len(matrix)//2]=b
for j in range(len(matrix)):
        matrix[j][j]=b
for j in range(len(matrix)-1,0,-1):
        matrix[j][j]=b



for i in range(len(matrix)):
    print(' '.join(map(str, matrix[i])))

