list1 = [int(i) for i in input().split()]
list2=[]
a = list1[0]
for j in range(len(list1)):
    for i in range(len(list1)):
        if a < list1[i]:
            a = list1[i]
            list1.pop(a)
            list2.append(a)
print(list2)
