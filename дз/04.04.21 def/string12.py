password=str(input())
c=0
if len(password)>=8:
    c+=1
for i in range(len(password)):
    if password[i].isupper():
        c+=1
        break
for i in range(len(password)):
    if password[i].islower():
        c+=1
        break
for i in range(len(password)):
    if password[i].isdigit():
        c+=1
        break
if c==4:
    print('password is good')
else:
    print('password is bad')
