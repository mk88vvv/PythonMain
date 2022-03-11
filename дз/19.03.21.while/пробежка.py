x = int(input())  # пробежал в 1 день
y = int(input())  # сколько должен пробежать
while x < y:
    x = x*1.1
    print(x)
print(x//10)
