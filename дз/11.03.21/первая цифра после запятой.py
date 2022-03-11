import math
a = float(input())
if type(a) is float:
    print('continue')
else:
    print('shsh')
    quit()
x, z = math.modf(a)
x = str(x)
print(x[2:-15])
