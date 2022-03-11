try:
    p1 = int(5)  # после 1,3,5 уроков
    p2 = int(15)  # после 2,3,4 уроков
    les = int(45)
    start = int(540)  # в минутах
    number = int(input('Введите номер урока'))
except ValueError:
    print('только int')
if number < 1 or number > 10:
    print('Не соблюдено условие')
    quit()
if number % 2 == 1:
    end = start + (number * les) + (p1 * (number - 1))+(p2*(number-2))
    print(int(end//60))
elif number % 2 == 0:
    end = start+(number*les)+(p1*(number-1))
    quit()
