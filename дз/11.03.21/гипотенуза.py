import math
a = int(input())
b = int(input())
c = math.sqrt(a ** 2 + b ** 2)
if a > c or b > c or a**2+b**2 > c**2:
    print('невозможно')
    quit()
else:
    print(c)
