a = int(input("Длина:"))  # в дольках
b = int(input("Ширина:"))  # в дольках
print("Количество долек в шоколадке:", a * b)
c = int(input("Искомые дольки:"))  # искомые дольки
if a != b and not c > a * b and a % 2 == 0 and c == a * b / 2:
    print("yes")
else:
    print("no")
