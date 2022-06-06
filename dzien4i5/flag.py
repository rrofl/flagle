import random
import os
from tkinter import *
from PIL import ImageTk, Image

path = os.chdir(os.getcwd() + '/flags')
window = Tk()
window.title("Flagle")
window.geometry("800x435")
window.configure(background="black")
window.iconbitmap("domciaPolsat.ico")
tablica_liczb = []
tablica_panstw = []
tablica_nazw = []

def new_img():
    files = os.listdir(path)
    flag = random.choice(files)
    global nazwa
    nazwa = os.path.splitext(flag)[0]
    print(os.path.splitext(flag)[0])
    return flag
        
def update_the_picture():
    myimg = new_img()
    updated_picture = ImageTk.PhotoImage(Image.open(myimg).resize((600, 338)), Image.Resampling.BICUBIC)
    w.image = updated_picture
    w.configure(image = updated_picture)

def check(*args):
    global panstwo
    panstwo = b.get()
    podane_kraje1 = Label(window, text=panstwo)
    podane_kraje2 = Label(window, text=panstwo)
    podane_kraje3 = Label(window, text=panstwo)
    podane_kraje4 = Label(window, text=panstwo)
    podane_kraje5 = Label(window, text=panstwo)
    podane_kraje1.place_forget()
    podane_kraje2.place_forget()
    podane_kraje3.place_forget()
    podane_kraje4.place_forget()
    podane_kraje5.place_forget()
    podane_kraje1.config(bg = "black", fg = "white")
    podane_kraje2.config(bg = "black", fg = "white")
    podane_kraje3.config(bg = "black", fg = "white")
    podane_kraje4.config(bg = "black", fg = "white")
    podane_kraje5.config(bg = "black", fg = "white")
    czarna_zaslona = Label(window, height = 150, width = 40)
    czarna_zaslona.config(bg = "black")
    gratulacje = Label(window, text = "Brawo 5Head'zie!")
    if panstwo == nazwa:
        b.delete(0, END)
        update_the_picture()
        cover()
        tablica_liczb.clear()
        tablica_panstw.clear()
        gratulacje.place(x = 260, y = 400)
        gratulacje.config(bg = "black", fg = "white")
        czarna_zaslona = Label(window, text = "            ", height = 150, width = 40)
        czarna_zaslona.config(bg = "black", fg = "black")
        czarna_zaslona.place(x = 650, y = 50)
    else:
        b.delete(0, END)
        cover_forget()
        if len(tablica_panstw) == 0:
            podane_kraje1.place(x = 650, y = 50)
            tablica_panstw.append(1)
        elif len(tablica_panstw) == 1:
            podane_kraje2.place(x = 650, y = 70)
            tablica_panstw.append(2)
        elif len(tablica_panstw) == 2:
            podane_kraje3.place(x = 650, y = 90)
            tablica_panstw.append(3)
        elif len(tablica_panstw) == 3:
            podane_kraje4.place(x = 650, y = 110)
            tablica_panstw.append(4)
        elif len(tablica_panstw) == 4:
            podane_kraje5.place(x = 650, y = 130)
            tablica_panstw.append(5)
        gratulacje.place_forget()
        czarna_zaslona.place(x = 500, y = 400)
        czarna_zaslona.place(x = 260, y = 400)
window.bind("<Return>", check)

def cover():
    top_left.place(x = 10, y = 10)
    top_mid.place(x = 210, y = 10)
    top_right.place(x = 410, y = 10)
    bot_left.place(x = 10, y = 179)
    bot_mid.place(x = 210, y = 179)
    bot_right.place(x = 410, y = 179)

def cover_forget():
    if len(tablica_liczb) != 6:
        i = random.randint(0, 5)
        if (i == 0) and (i not in tablica_liczb):
            top_left.place_forget()
            tablica_liczb.append(0)
        elif (i == 1) and (i not in tablica_liczb):
            top_mid.place_forget()
            tablica_liczb.append(1)
        elif (i == 2) and (i not in tablica_liczb):
            top_right.place_forget()
            tablica_liczb.append(2)
        elif (i == 3) and (i not in tablica_liczb):
            bot_left.place_forget()
            tablica_liczb.append(3)
        elif (i == 4) and (i not in tablica_liczb):
            bot_mid.place_forget()
            tablica_liczb.append(4)
        elif (i == 5) and (i not in tablica_liczb):
            bot_right.place_forget()
            tablica_liczb.append(5)
        else:
            cover_forget()
    else:
        nazwa_panstwa = Label(window, text="", bg = "black", fg="white")
        nazwa_panstwa.place_forget()
        nazwa_panstwa.place(x = 500, y = 400)
        if len(tablica_nazw) != 1:
            nazwa_panstwa.config(text=nazwa)
            tablica_nazw.append(1)
        else:
            nazwa_panstwa.config(text="")
            tablica_nazw.clear()

myimg = new_img()
img = ImageTk.PhotoImage(Image.open(myimg).resize((600, 338)), Image.Resampling.BICUBIC)
w = Label(window, image = img)
w.place(x = 10, y = 10)
b = Entry(window, width=50, font=("Calibri", 12), justify="center")
b.place(x = 100, y = 360)
wypisane_kraje = Label(window, text = "Ostatnie państwo: ")
wypisane_kraje.config(bg = "black", fg="white")
wypisane_kraje.place(x = 650, y = 30)
zaslona = ImageTk.PhotoImage(Image.open("white.jpg").resize((200, 169)), Image.Resampling.BICUBIC)
gratulacje = Label(window, text = "")
top_left = Label(window, image = zaslona)
top_left.place(x = 10, y = 10)
top_mid = Label(window, image = zaslona)
top_mid.place(x = 210, y = 10)
top_right = Label(window, image = zaslona)
top_right.place(x = 410, y = 10)
bot_left = Label(window, image = zaslona)
bot_left.place(x = 10, y = 179)
bot_mid = Label(window, image = zaslona)
bot_mid.place(x = 210, y = 179)
bot_right = Label(window, image = zaslona)
bot_right.place(x = 410, y = 179)

window.mainloop()