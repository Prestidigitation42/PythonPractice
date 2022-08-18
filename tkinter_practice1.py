'''
Created on Jul 30, 2022

@author: nstru

Source: https://www.youtube.com/watch?v=YXPyB4XeYLA&t=637s
'''

from tkinter import *

root = Tk()

e = Entry(root, width=50, fg="#ffffff", bg="#000000")
e.pack()
e.insert(0, "Enter Your Name")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name!", command=myClick, fg="black", bg="#ffffff")
myButton.pack()

root.mainloop()