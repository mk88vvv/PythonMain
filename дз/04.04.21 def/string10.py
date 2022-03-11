string1='In the hole in the ground there lived a hobbit'
string2=''
c='H'
for i in range(string1.index('h')+1,string1.rindex('h')):
    if string1[i]=='h':
        string2+=c
    else:
        string2+=string1[i]
print(string1[:string1.index('h')+1] + string2+string1[string1.rindex('h'):])
        
