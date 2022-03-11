import math


def distance():
    if x1 > x2:
        kx = x1 - x2
    else:
        kx = x2 - x1
    if y1 > y2:
        ky = y1 - y2
    else:
        ky = y2 - y1
    gip = math.sqrt(kx ** 2 + ky ** 2)
    print(round(gip, 4))


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
distance() 
