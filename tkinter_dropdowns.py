'''
Created on Aug 8, 2022

@author: nstru
'''

from tkinter import *

root = Tk()
root.title("Learning tkinter Sliders")
root.geometry("400x400")


def show():
    my_label = Label(root, text=clicked.get()).pack()
    
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()


my_btn = Button(root, text="Show Selection", command=show).pack()

root.mainloop()