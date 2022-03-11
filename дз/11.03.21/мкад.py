a = 109000
V = int(input())
t = int(input())  # в часах,поэтому инт.
S = V*t
if t < 1 or S < -108 or S > 108:
    print('не соблюдено условие')  # время не может быть меньше единицы
    quit()
else:
    print(S)
