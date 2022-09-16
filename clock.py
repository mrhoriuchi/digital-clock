from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

Label(root, font=("Arial", 20), text = "Royal Clock", background = "black", foreground = "gold").pack()
label = Label(root, font=("Arial", 80), background = "black", foreground = "gold")
label.pack(anchor='center')
time()

mainloop()
