n = int(input())
a = 1
b=[]
for i in range(1,n+1):
    a = a * i
    b.append(a)
print(sum(b))

