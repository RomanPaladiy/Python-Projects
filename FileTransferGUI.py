# Importing the required Libraries
import tkinter
from tkinter import *
from tkinter import  filedialog
import shutil
import os
import datetime
import time 

from numpy import pad

def source_directory():
        dirName = filedialog.askdirectory()
        sourceDir.delete(0,END)
        sourceDir.insert(0,dirName)


def destination_directory():
        dirName = filedialog.askdirectory()
        destinationDir.delete(0,END)
        destinationDir.insert(0,dirName)


m = tkinter.Tk()

# Creating a basic tkinter window

# Design/sizing of the window
m.minsize(750,150)
m.title('File Transfer')
m.config(bg='LightGray')



# Creating a button
button1 = Button(m, text= "Browse", padx=20, command=source_directory)
button1.grid(row=0, column=0,padx=(20,10),pady=(30,0))
sourceDir = Entry(m,width=100)
sourceDir.grid(row=0, column=1,padx=20,pady=(30,0), sticky=E)


# Creating the second button 
button2 = Button(m, text= "Browse",  padx=20, command=destination_directory)
button2.grid(row=0, column=0,padx=(20,10),pady=(100,0))
destinationDir = Entry(m,width=100)
destinationDir.grid(row=0, column=1, padx=20,pady=(100,0), sticky=E)


m.mainloop()

        









