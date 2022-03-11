from tkinter import *
import button
##############
n = 0


def destroy_button_modified():
    destroy_button(b)   


def counter():
    global n
    n += 1
    button.lll1(n)


def window():
    global tk
    tk = Tk()
    tk.title("Планировщик")
    btn1 = Button(tk, text="Добавить задачу",
                  command=counter,
                  activeforeground="lightgreen",
                  fg="DarkSlateGray4",
                  bg="lightgrey",
                  width="30",
                  font="TimesNewRoman 30")
    # deletebtn = Button(bg="red", fg="white", font="25", text="X", height="3", width="3",command=btnname.destroy)
    btn1.pack()
    tk.mainloop()


window()
не активен№№№№№№№№№№№№№№№№№№№