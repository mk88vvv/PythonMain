try:
    h1 = int(input())  # часы
    m1 = int(input())  # минуты
    s1 = int(input())  # секунды
    h2 = int(input())  # часы
    m2 = int(input())  # минуты
    s2 = int(input())  # секунды
except ValueError:
    print('Только int')
    quit()
if h1 >= 24 or h2 >= 24 or m1 >= 60 or m2 >= 60 or s1 >= 60 or s2 >= 60:
    print('ошибка')
    quit()
x1 = h1 * 60 * 60 + m1 * 60 + s1
x2 = h2 * 60 * 60 + m2 * 60 + s2
if x1 == x2:
    print(0)
    quit()
elif x1 > x2:
    print(int(x1 - x2))
else:
    print(int(x2 - x1))
    print(h1, end='h2-2')
    print(h2*s2)
