import random
import os
import tkinter as tk
from PIL import ImageTk, Image

path = os.chdir(os.getcwd() + '/flags')
window = tk.Tk()
window.title("Flagle")
window.geometry("600x400")
window.configure(background="white")

def new_img():
    files = os.listdir(path)
    flag = random.choice(files)
    global nazwa
    nazwa = os.path.splitext(flag)[0]
    print(os.path.splitext(flag)[0])
    return flag

def update_the_picture():
    myimg = new_img()
    updated_picture = ImageTk.PhotoImage(Image.open(myimg).resize((400, 225)), Image.Resampling.BICUBIC)
    w.configure(image = updated_picture)
    w.image = updated_picture

def check():
    if str(b.get()) == str(nazwa):
        os.system('cls')
        b.delete(0, tk.END)
        update_the_picture()
    else:
        print("zle")
    

myimg = new_img()
img = ImageTk.PhotoImage(Image.open(myimg).resize((400, 225)), Image.Resampling.BICUBIC)

w = tk.Label(window, image = img)
b = tk.Entry(window, width=20, font=("LEMON MILK Medium", 12), justify="center")

w.pack(side = "top", expand="yes")
b.pack(side = "bottom", padx=10, pady=20)
submit_button = tk.Button(window, text="Sprawdź", width=10, command=check).pack(side='bottom')

window.mainloop()