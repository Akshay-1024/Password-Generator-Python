import random
from tkinter import *
from tkinter import messagebox

top = tkinter.Tk()
def pwd():
    lower   = "abcdefghijklmnopqrstuvwxyz"
    upper   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbes  = "0123456789"
    symbols = "[]{};()_-+@"

    all = lower + upper + numbes + symbols

    length = 16
    password = "".join(random.sample(all,length))
    return password

def getpass():
    x = pwd()
    msg = messagebox.showinfo( "password generator", x)

B = Button(top, text = "Hello", command = getpass)
B.place(x = 50,y = 50)


top.mainloop()
