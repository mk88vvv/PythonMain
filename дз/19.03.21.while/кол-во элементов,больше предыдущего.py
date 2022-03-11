a = int(input())
b = 0
с = 0
while a != 0:
    b = a
    a = int(input())
    if b < a:
        с = с + 1
print(с)
