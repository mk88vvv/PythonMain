string1 = 'hhelloo'

for i in range(len(string1)):
    c=0
    for j in range(len(string1)):
        if string1[i] == string1[j]:
            c += 1
    if c == 1:
        print(string1[i])
        
