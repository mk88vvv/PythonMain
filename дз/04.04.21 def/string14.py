string1 = 'HeLLO WOrld'
c = 0
for i in range(len(string1)):
    if string1[i].isupper():
        c += 1
    else:
        c -= 1
if c > 0:
    b = string1.upper()
    print(b)
else:
    b = string1.lower()
    print(b)
