string1='Bananas, give me bananas!!!'
string2='banana bananas'
string3=string2.split()
c=0
for i in range(len(string3)):
    if string3[i] in string1:
        c+=1
print(c)