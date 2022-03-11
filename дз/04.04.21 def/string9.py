string1='bilbo.baggins@bagend.hobbiton.shire.me'
string2=''
for i in range(len(string1)):
    if string1[i]!='@':
        string2+=string1[i]
print(string2)
        
