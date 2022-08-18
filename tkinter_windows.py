'''
Created on Aug 4, 2022

@author: nstru
'''

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning tkinter Windows")

def open():
    global my_img
    top = Toplevel()
    top.title("Second Window")
    my_img = ImageTk.PhotoImage(Image.open("C:/Users/nstru/OneDrive/Pictures/Chess_Matching.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()



root.mainloop()