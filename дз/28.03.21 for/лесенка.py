a = int(input())  # n чисел
i = 0
if a > 9:
    quit
b = []
for i in range(a):
    i += 1
    b.append(i)
    print(*b)

