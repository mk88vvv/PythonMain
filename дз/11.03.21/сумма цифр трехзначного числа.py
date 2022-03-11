a = int(input())
if len(str(a)) == 3:
    list(str(a))
    print(sum((list(str(a)))))
else:
    # спросить как работает end в print
    print('Введите трехзначное число', end='sd')
    quit()
