n = int(input())  #число,возводимое в степень
b=[]
for i in range(1,n+1):
    b.append(i**2)
print(sum(b))
