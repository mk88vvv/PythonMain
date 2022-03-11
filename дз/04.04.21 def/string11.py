string1 = 'Python'
string2 = ''
for i in range(len(string1)):
    if i % 3 == 0:
        string2+=''
    else:
        string2+=string1[i]
print(string2)