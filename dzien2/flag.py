import random
import os
from tkinter import *
from PIL import ImageTk, Image

path = os.chdir(os.getcwd() + '/flags')
window = Tk()
window.title("Flagle")
window.geometry("800x450")
window.configure(background="black")

def new_img():
    files = os.listdir(path)
    flag = random.choice(files)
    if flag != "botleft.png" or "botmid.png" or "botright.png" or "topleft.png" or "topmid.png" or "topright.png":
        global nazwa
        nazwa = os.path.splitext(flag)[0]
        print(os.path.splitext(flag)[0])
        return flag
        
def update_the_picture():
    myimg = new_img()
    updated_picture = ImageTk.PhotoImage(Image.open(myimg).resize((600, 338)), Image.Resampling.BICUBIC)
    w.configure(image = updated_picture)
    w.image = updated_picture

def check(*args):
    if b.get() == nazwa:
        b.delete(0, END)
        update_the_picture()
    else:
        b.delete(0, END)
window.bind("<Return>", check)

myimg = new_img()
img = ImageTk.PhotoImage(Image.open(myimg).resize((600, 338)), Image.Resampling.BICUBIC)
zaslona = ImageTk.PhotoImage(Image.open("white.jpg").resize((210, 169)), Image.Resampling.BICUBIC)

w = Label(window, image = img)
w.place(x = 10, y = 10)
b = Entry(window, width=50, font=("Calibri", 12), justify="center")
b.place(x = 100, y = 360)
submit_button = Button(window, text="Sprawdź", width=10, command=check)
submit_button.place(x = 260, y = 400)
"""
top_left = Label(window, image = zaslona)
top_left.place(x = 10, y = 10)
top_mid = Label(window, image = zaslona)
top_mid .place(x = 200, y = 10)
top_right = Label(window, image = zaslona)
top_right.place(x = 400, y = 10)
bot_left = Label(window, image = zaslona)
bot_left.place(x = 10, y = 179)
bot_mid = Label(window, image = zaslona)
bot_mid.place(x = 200, y = 179)
bot_right = Label(window, image = zaslona)
bot_right.place(x = 400, y = 179)
"""

window.mainloop()