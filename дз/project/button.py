from tkinter import *
from main import destroy_button

def lll1(n):
    zadacha(n)
    vvod()
    delete()
    # week()


def zadacha(n):
    stroka1 = Label(width=17, height=3, bg='lightgreen', text=f"Задача {n}")
    stroka1.pack()  # stroka1.place(x=5,y)stroka1.place(x=30,y=30)


def vvod():
    global vvod1
    vvod1 = Entry(fg="red")  # тут пишется сама задача
    vvod1.pack()



def delete(i,j,vvod1,zadacha1,): 
    deletebtn = Button(bg="brown1",
fg="white",
font="25",
    text="X",
height="1",
width="12",
command=lambda: destroy_button(vvod1,zadacha1,deletebtn))
    deletebtn.grid(row=i+2,column=j)


