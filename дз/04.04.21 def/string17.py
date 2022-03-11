string1='Я иду с мечем судия'
string2=string1[::-1].lower().split()
string1=string1.lower().split()
string1=''.join(string1)
string2=''.join(string2)

if string2==string1:
    print('DA')
else:
    print('NET')