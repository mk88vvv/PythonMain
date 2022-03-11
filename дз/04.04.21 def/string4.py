string = 'asdflkqpoifoasd'
count = 0
for i in range(len(string)):
    if string[i] == 'f':
        count += 1
if count == 1:
    print(string.index('f'))
elif count > 1:
    print(string.index('f'), string.rindex('f'))
