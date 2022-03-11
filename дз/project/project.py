#########
import random
import random
from tkinter import *  
#########
def button1_clicked():
    bone_1 = int(random.uniform(1, 7))
    bone_2 = int(random.uniform(1, 7))
    print("bone_1=", bone_1, "\nbone_2=", bone_2, "\nsum of bones=", bone_1 + bone_2, "\n*****")

        
            
    
    

def window():  
    window = Tk()
    window.title("Игра в кости")
    btn1 = Button(window, text="Брошены",
    command=button1_clicked,
    activeforeground="grey",
    bg="red",
    fg="red",
    width="25",
    font="TimesNewRoman 30")
    btn1.pack()
    global wtext
    wtext = Canvas(window, width=500, height=200)
    wtext.pack()
    wtext.create_text(250, 50, text="Для того, чтобы бросить кости, нажмите на кнопку", fill="blue", font="TimesNewRoman 15")
    window.mainloop()
    return (wtext, window)

window()

не активен№№№№№№№№№№№№№№№№№№№