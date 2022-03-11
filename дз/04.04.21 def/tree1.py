tree = {}
n = 9
for i in range(n-1):
    child, parent = input().split()
    tree[child] = parent
print(tree)
request = 3
for i in range(request):
    child1, parent1 = input().split()
    n = child1
    while n in tree:
        n = tree[n]
        c = 0
        if n == parent1:
            print('2')
            c += 1
    m = parent1
    while m in tree:
        m = tree[m]
        if m == child1:
            print('1')
            c += 1
    if c == 0:
        print('0')
