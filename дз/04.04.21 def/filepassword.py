l = open("login.txt")
p = open("password.txt")
a = input()
b = input()
ll = l.readline()
pp = p.readline()
if a == ll and b == pp: 
    print("вход выполнен")
else:
    print("данные введены неверно")
l.close()
p.close()
