rows = 8
tree = {}
for i in range(rows):
    n=input().split()
    tree[n[0]]=n[1]
    
print(tree)
child1=input()
count1=0
if child1 in tree:
    count1+=1
print(count1)
