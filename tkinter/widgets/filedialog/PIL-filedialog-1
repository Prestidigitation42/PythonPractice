'''
Created on Aug 4, 2022

@author: nstru
'''

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from pip._internal.utils import filetypes

root = Tk()
root.title("Learning tkinter filedialog")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/nstru/OneDrive/Pictures/",
                                              title = "Select A File",
                                              filetypes=(("jpg files", "*.jpg"),
                                                         ("all files", "*.*")))
    
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

btn = Button(root, text="Open File", command=open).pack()

root.mainloop()
