# """ Historial """
# #https://github.com/Pizaguerri/Bootcamp_Fundesplai-Treball_Final
# import os
# from tkinter import *

# main = Tk()



# main.mainloop()

#Import the library
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win= Tk()

#Set the window geometry
win.geometry("750x250")

#Display a Label
def print_text(text):
   Label(win, text=text,font=('Helvetica 13 bold')).pack()

btn1= ttk.Button(win, text="Button1" ,command= lambda:
print_text("Button 1"))
btn1.pack(pady=10)
btn2= ttk.Button(win, text="Button2" ,command= lambda:
print_text("Button 2"))
btn2.pack(pady=10)
btn3= ttk.Button(win, text="Button3" ,command= lambda:
print_text("Button 3"))
btn3.pack(pady=10)

win.mainloop()