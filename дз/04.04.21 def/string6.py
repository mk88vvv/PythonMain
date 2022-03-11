string1='In the hole in the ground there lived a hobbit'
string2=''
string3=''
string4=''
for i in range (string1.index('h')):
    string2+=string1[i]
for i in range(string1.rindex('h')+1,len(string1)):
    string3+=string1[i]
string4=string2+string3

print(string4)

