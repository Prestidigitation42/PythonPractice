'''
Created on Aug 3, 2022

@author: nstru
'''

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learning tkinter Messages")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is the text", "This is the message")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked Yes!").pack()
    else:
        Label(root, text="You clicked No!").pack()
        
        
Button(root, text="Popup", command=popup).pack()



root.mainloop()
