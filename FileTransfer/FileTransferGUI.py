# Importing the required Libraries
import tkinter
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile

# Creating a basic tkinter window
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__ (self)


# Design/sizing of the window
        self.master = master
        self.master.resizable(width= True, height= True)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('File Transfer')
        self.master.config(bg='LightGray')


        # Adding labels in the widget
        self.lblDisplay = Label(self.master, text= "Click Button to Browse Files.", font =('Helvetica',16),fg="black",bg="LightGray")
        self.lblDisplay.pack(pady=10)


        def open_file():
            file = filedialog.askopenfile(mode='r', filetypes=[('Text Files' , '*.txt')])
            if file:
                content = file.read()
                file.close()
                



# Creating a button
        ttk.Button(self.master, text= "Browse", command=open_file).pack(pady=20)


        



            
        

















if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()










    
