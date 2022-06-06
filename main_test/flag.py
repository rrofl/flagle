import random
import os
from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image

path = os.chdir(os.getcwd() + '/flags')
window = Tk()
window.title("Flagle")
window.geometry("1280x720")
window.configure(bg = "#121212")
window.iconbitmap("domciaPolsat.ico")
tablica_liczb = []
tablica_panstw = []
tablica_nazw = []

def new_img():
    flag = random.choice(os.listdir(path))
    if flag.endswith(".png"):
        global nazwa
        nazwa = os.path.splitext(flag)[0]
        print(os.path.splitext(flag)[0])
        return flag
    else:
        new_img()

def update_the_picture():
    updated_picture = ImageTk.PhotoImage(Image.open(new_img()).resize((1056, 594)), Image.Resampling.BICUBIC)
    w.image = updated_picture
    w.configure(image = updated_picture)

def check(*args):
    panstwo = b.get()
    wybrane_panstwo = wysuwana_lista.get()
    podane_kraje1 = Label(window, text=panstwo or wybrane_panstwo, bg = "#121212", fg = "white")
    podane_kraje2 = Label(window, text=panstwo or wybrane_panstwo, bg = "#121212", fg = "white")
    podane_kraje3 = Label(window, text=panstwo or wybrane_panstwo, bg = "#121212", fg = "white")
    podane_kraje4 = Label(window, text=panstwo or wybrane_panstwo, bg = "#121212", fg = "white")
    podane_kraje5 = Label(window, text=panstwo or wybrane_panstwo, bg = "#121212", fg = "white")
    czarna_zaslona1 = Label(window, width = 30, height = 50, bg = "#121212")
    czarna_zaslona2 = Label(window, width = 15, height = 5, bg = "#121212")
    czarna_zaslona3 = Label(window, width = 50, height = 5, bg = "#121212")
    nazwa_panstwa = Label(window, text = "", bg = "#121212", fg = "white")
    nazwa_panstwa.place(x = 660, y = 680)
    if (panstwo == nazwa):
        podane_kraje1.place_forget()
        podane_kraje2.place_forget()
        podane_kraje3.place_forget()
        podane_kraje4.place_forget()
        podane_kraje5.place_forget()
        nazwa_panstwa.place_forget()
        nazwa_panstwa.config(text = "")
        b.delete(0, END)
        update_the_picture()
        cover()
        tablica_liczb.clear()
        tablica_panstw.clear()
        gratulacje = Label(window, text = "Brawo 5Head'zie!", bg = "#121212", fg = "white")
        gratulacje.place(x = 140, y = 400)
        czarna_zaslona1.place(x = 630, y = 50)
        czarna_zaslona3.place(x = 400, y = 400)
    elif (wybrane_panstwo == nazwa):
        podane_kraje1.place_forget()
        podane_kraje2.place_forget()
        podane_kraje3.place_forget()
        podane_kraje4.place_forget()
        podane_kraje5.place_forget()
        nazwa_panstwa.place_forget()
        nazwa_panstwa.config(text = "")
        b.delete(0, END)
        update_the_picture()
        cover()
        tablica_liczb.clear()
        tablica_panstw.clear()
        gratulacje = Label(window, text = "Brawo 5Head'zie!", bg = "#121212", fg = "white")
        gratulacje.place(x = 140, y = 400)
        czarna_zaslona1.place(x = 630, y = 50)
        czarna_zaslona3.place(x = 400, y = 400)
    else:
        b.delete(0, END)
        cover_forget()
        if len(tablica_panstw) == 0:
            podane_kraje1.place(x = 1110, y = 50)
            tablica_panstw.append(0)
        elif len(tablica_panstw) == 1:
            podane_kraje2.place(x = 1110, y = 70)
            tablica_panstw.append(1)
        elif len(tablica_panstw) == 2:
            podane_kraje3.place(x = 1110, y = 90)
            tablica_panstw.append(2)
        elif len(tablica_panstw) == 3:
            podane_kraje4.place(x = 1110, y = 110)
            tablica_panstw.append(3)
        elif len(tablica_panstw) == 4:
            podane_kraje5.place(x = 1110, y = 130)
            tablica_panstw.append(4)   
        elif len(tablica_panstw) == 5:
            podane_kraje5.place(x = 1110, y = 150)
            tablica_panstw.append(5)   
        elif len(tablica_panstw) == 6:
            podane_kraje5.place(x = 1110, y = 170)
            tablica_panstw.append(6)   
            nazwa_panstwa.config(text = "Jest to flaga państwa: " + nazwa)
        czarna_zaslona2.place(x = 140, y = 400)
        variable.set("")
window.bind("<Return>", check)

def cover():
    top_left.place(x = 10, y = 10)
    top_mid.place(x = 364, y = 10)
    top_right.place(x = 718, y = 10)
    bot_left.place(x = 10, y = 307)
    bot_mid.place(x = 364, y = 307)
    bot_right.place(x = 718, y = 307)

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

img = ImageTk.PhotoImage(Image.open(new_img()).resize((1056, 594)), Image.Resampling.BICUBIC)
w = Label(window, image = img)
w.place(x = 10, y = 10)
b = Entry(window, width = 60, font = ("Calibri", 14), justify = "center")
b.place(x = 20, y = 620)
c = Label(window, text = "Wybór państwa ->", bg = "#121212", fg = "white")
c.place(x = 660, y = 623)
wypisane_kraje = Label(window, text = "Ostatnie państwa: ", bg = "#121212", fg="white")
wypisane_kraje.place(x = 1125, y = 30)
OPTIONS = [
    'afganistan', 'albania', 'algieria', 'andora', 'anglia', 'angola', 'arabia saudyjska', 'argentyna', 'armenia', 'aruba', 'australia', 'austria', 'azerbejdzan', 'bahamy', 'bahrajn', 'bangladesz', 'barbados', 'belgia', 'belize', 'benin', 'bermudy', 'bhutan', 'bialorus', 'boliwia', 'bosnia i herzegowina', 'botswana', 'brazil', 'brunei', 'burkina faso', 'bułgaria', 'chile', 'chiny', 'chorwacja', 'cyprus', 'czarnogora', 'czechy', 'dania', 'demokratyczna republika konga', 'dominika', 'dominikana', 'dzibuti', 'egipt', 'ekwador', 'erytrea', 'estonia', 'etiopia', 'filipiny', 'finlandia', 'francja', 'gabon', 'gambia', 'ghana', 'gibraltar', 'grecja', 'grenada', 'grenlandia', 'gruzja', 'guam', 'gujana', 'gwatemala', 'gwinea bissau', 'gwinea', 'haiti', 'hiszpania', 'honduras', 'hongkong', 'indie', 'indonezja', 'irak', 'iran', 'irlandia polnocna', 'irlandia', 'islandia', 'izrael', 'jamajka', 'japonia', 'jemen', 'jordania', 'kambodza', 'kamerun', 'kanada', 'katar', 'kazachstan', 'kenia', 'kirgistan', 'kolumbia', 'kongo', 'korea polnocna', 'korea poludniowa', 'kosowo', 'kostaryka', 'kuba', 'kuwejt', 'laos', 'lesotho', 'liban', 'liberia', 'libia', 'liechtenstein', 'litwa', 'lotwa', 'luksemburg', 'macedonia polnocna', 'madagaskar', 'majotta', 'malawi', 'malediwy', 'malezja', 'mali', 'malta', 'maroko', 'mauretania', 'mauritius', 'meksyk', 'mjanma', 'moldawia', 'monako', 'mongolia', 'mozambik', 'namibia', 'nauru', 'nepal', 'niderlandy', 'niemcy', 'niger', 'nigeria', 'nikaragua', 'norwegia', 'nowa kaledonia', 'nowa zelandia', 'oman', 'pakistan', 'palau', 'palestyna', 'panama', 'papua nowa gwinea', 'paragwaj', 'peru', 'polska', 'portoryko', 'portugalia', 'republika poludniowej afryki', 'rosja', 'rumunia', 'rwanda', 'salwador', 'san marino', 'senegal', 'serbia', 'sierra leone', 'singapur', 'slowacja', 'slowenia', 'somalia', 'stany zjednoczone', 'sudan poludniowy', 'sudan', 'surinam', 'syria', 'szkocja', 'szwajcaria', 'szwecja', 'tadzykistan', 'tajlandia', 'tajwan', 'tanzania', 'timor wschodni', 'togo', 'tonga', 'trynidad i tobago', 'tunezja', 'turcja', 'turkmenistan', 'uganda', 'ukraina', 'urugwaj', 'uzbekistan', 'walia', 'watykan', 'wegry', 'wenezuela', 'wielka brytania', 'wietnam', 'wlochy', 'wybrzeze kosci sloniowej', 'wyspy owcze', 'zambia', 'zimbabwe', 'zjednoczone emiraty arabskie'
]
variable = StringVar()
variable.set("")
wysuwana_lista = Combobox(window, textvariable = variable, values = OPTIONS, width = 45)
wysuwana_lista.place(x = 770, y = 623)
wysuwana_lista.bind('<<ComboboxSelected>>', check)
wybrane_panstwo = wysuwana_lista.get()
zaslona = ImageTk.PhotoImage(Image.open("black.jpg").resize((352, 297)), Image.Resampling.BICUBIC)
top_left = Label(window, image = zaslona)
top_left.place(x = 10, y = 10)
top_mid = Label(window, image = zaslona)
top_mid.place(x = 364, y = 10)
top_right = Label(window, image = zaslona)
top_right.place(x = 718, y = 10)
bot_left = Label(window, image = zaslona)
bot_left.place(x = 10, y = 307)
bot_mid = Label(window, image = zaslona)
bot_mid.place(x = 364, y = 307)
bot_right = Label(window, image = zaslona)
bot_right.place(x = 718, y = 307)

window.mainloop()