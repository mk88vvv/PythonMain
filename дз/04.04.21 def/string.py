string1='kiaksdj123'
print(string1[2])
print(string1[8])
print(string1[0:5])
print(string1[0:8])
for i in range(0,len(string1),2):
    print(string1[i],end=' ')
print(' ')
for i in range(1,len(string1),2):
    print(string1[i],end=' ')
print(' '
)
for i in range(len(string1)-1,-1,-1):
    print(string1[i],end='')
print(' ')
print(string1[::-2])
print(len(string1))
