# def swap_columns(a, i, j):
a = []
m = 3
n = 3
i, j = map(int, input().split())
if i < 4 and j < 4 and i > 0 and j > 0:
    print(i, j)
else:
    quit()
count = 0
for i in range(m):
    row = []
    for j in range(n):
        row.append(count)
        count += 1
    a.append(row)
for i in range(len(a)):
    print(' '.join(map(str, a[i])))
for i in range (m):
    z = a[i-1,i-1]
    
# swap_columns()
