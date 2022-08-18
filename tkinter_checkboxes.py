'''
Created on Aug 8, 2022

@author: nstru
'''

from tkinter import *

root = Tk()
root.title("Learning tkinter Sliders")
root.geometry("400x400")


def show():
    my_label = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()



my_btn = Button(root, text="Show Selection", command=show).pack()


root.mainloop()