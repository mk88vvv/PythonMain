import math
try:
    a = int(input())  # руб
    b = int(input())  # коп
    n = int(input())  # пирожков
except ValueError:
    print('только int')
if b > 100:
    print('Невозможно')
    quit()
else:
    a = float(a*100)
    price = n * (a + b)
    print(price, 'копеек,или')
price = price / 100
x, z = math.modf(price)
print(int(z), 'руб', int(round(x, 1)*10), 'коп')
