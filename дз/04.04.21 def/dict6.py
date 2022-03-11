len1=5
words1={}
a = input().split()
for i in range(len(a)):
    if a[i] in words1:
        words1[a[i]]+=1
    else:
        words1[a[i]]=1
print(words1)

