words=["Treasure","Island","is","an","adventure","novel","by","Scottish","author",
"Robert","Louis","adventure","author","author","Island","adventure","novel","adventure"]
nums=[]
temp=[]
for i in range(len(words)):
    c=0
    for j in range(len(words)):
        if words[i]==words[j]:
            c+=1
    if c>0 and words[i] not in temp:
        nums.append(c)
        temp.append(words[i])
    
print(nums)
print(temp)    


        