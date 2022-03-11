files = 4
dictfiles = {}
count = 0
for i in range(files):
    filename, *operations = input().split()
    dictfiles[filename] = operations
print(dictfiles)
print("[файл] - [действие]")
fname, operation = input().split()
for i in range(len(dictfiles[fname])):
    if dictfiles[fname][i] == operation:
        count+=1
if count==1:
    print('OK')
else:
    print('Access denied')