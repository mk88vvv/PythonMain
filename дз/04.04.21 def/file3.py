file1=open("file3.txt")
a=file1.readline()
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])
print(sum(a))
