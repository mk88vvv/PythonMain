
n = int(input())  #кол-во вводимых чисел
b=[]
for i in range(n+1):
    i = int(input())
    if i == 0:
        i=+1
        b.append(i)
print(sum(b))
