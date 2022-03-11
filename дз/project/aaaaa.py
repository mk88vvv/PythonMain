from tkinter import *
from button import *
root = Tk()
days = ["Понедельник", "Вторник", "Среда",
        "Четверг", "Пятница", "Суббота", "Воскресенье"]
#       0             1         2       3         4         5          6

for i in range(2, 20, 3):
    n=-1
    z=0
    for j in range(7):
        n+=1
        day=Label(text=f"{days[n]}",height=3,width=10)
        day.grid(row=z,column=j)
        zadacha1 = Label(text=f"Задача{i//2}",
        height=2,
        width=10,
        bg='lightgreen')
        zadacha1.grid(row=i, column=j)
        global vvod1
        vvod1 = Entry(bg="white",                               #ввод
        bd="2",
        justify="center",
        width="20") 
        vvod1.grid(row=i+1, column=j)
        delete(i, j, vvod1, zadacha1)

        #!TODO вернуть лейблы дни недели и кнопку звездочку


root.mainloop()