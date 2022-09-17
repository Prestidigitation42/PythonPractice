'''
Created on Jul 31, 2022

@author: nstru
'''

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning tkinter Labels")
root.iconbitmap('')


my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/nstru/OneDrive/Pictures/Chess_Matching.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/nstru/OneDrive/Pictures/Solar_System.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/nstru/OneDrive/Pictures/Solaris.jpg"))

image_list = [my_img1, my_img2, my_img3]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def back(image_num):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    button_forward = Button(root, text=">>", command=lambda:forward(image_num+1))
    button_back = Button(root, text="<<", command=lambda:back(image_num-1))
    
    if image_num == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    status = Label(root, text="Image " + str(image_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def forward(image_num):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    button_forward = Button(root, text=">>", command=lambda:forward(image_num+1))
    button_back = Button(root, text="<<", command=lambda:back(image_num-1))
    
    if image_num == 3:
        button_forward = Button(root, text=">>", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    status = Label(root, text="Image " + str(image_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop()
