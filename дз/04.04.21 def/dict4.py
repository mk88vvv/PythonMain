dict1={}
string1="apple orange banana banana orange"
string1=string1.split()
print(string1)
dict2=[]
for i in range(len(string1)):
    if string1[i] in dict1:
        dict1[string1[i]]+=1
    else:
        dict1[string1[i]]=1
print(dict1)
for i in dict1:
    if dict1[i] == max(dict1.values()):
        dict2.append(i)
dict2.sort()
print(dict2[0])

