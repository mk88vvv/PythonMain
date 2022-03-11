string1='1+1=2'
string2=''
c='one'
for i in range(len(string1)):
    if string1[i]=='1':
        string2+=c
    else:
        string2+=string1[i]
print(string2)
