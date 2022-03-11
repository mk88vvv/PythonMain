import math
a = float(input())
if type(a) is float:
    print('continue')
else:
    print('shshsh')
    quit()
# первый способ. Спросить про то,как работает = math.modf(a), почему в конце.
e, d = math.modf(a)
print(e)
print(d)
b = a-int(a)
print('SECOND', b)
