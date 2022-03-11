n = 9
matrix = []
row = []
a = '0'
b='2'
b = '1'
k=0
for i in range(n):
    row.append(a)
for i in range(n):
    matrix.append(row.copy())
for j in range(len(matrix)):
        matrix[j][len(matrix)-j-1]=b
for k in range(0,n-k,-1):
    matrix[-k]


print(type)

for i in range(len(matrix)):
    print(' '.join(map(str, matrix[i])))

