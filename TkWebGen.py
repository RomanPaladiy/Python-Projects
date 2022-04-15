import tkinter
import webbrowser
from tkinter import *

# Basic tkinter window
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)
# making the widget how I want it to look
        self.master = master
        self.master.resizable(width=False, height = False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('HTML File Changes')
        self.master.config(bg='lightgray')
                    
        self.varinput = StringVar()


        self.lblinput = Label(self.master,text='User Input: ', font=("Helvetica",16),fg="black",bg='Lightgray')
        self.lblinput.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font=("Helvetica",16),fg="black",bg='Lightgray')
        self.lblDisplay.grid(row=3,column=1,padx=(30,0),pady=(30,0))

        self.txtinput = Entry(self.master,text=self.varinput, font=("Helvetica",16),fg="black",bg='Lightblue')
        self.txtinput.grid(row=0,column=1,padx=(30,0),pady=(30,0))

        self.btnSubmit = Button(self.master,text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=1,padx=(0,0),pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master,text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=1,padx=(0,90),pady=(30,0), sticky=NE)

    

# submits the input from user
    def submit(self):
        ut = self.varinput.get()
        self.lblDisplay.config(text='Input Received!',fg="Green".format(ut))
        
# concatenating the strings together
        htmlCode1 = """<html>
                        <body>
                            <h1>"""
                         
        htmlCode2 = """</h1>
                        </body>
                      </html>"""
        
        htmlCodeFinal = htmlCode1 + ut + htmlCode2
          
        # defining the fileName to it can open it in google chrome
        fileName = 'webpage.html'

        f = open(fileName, 'w')
        f.write(htmlCodeFinal)
        f.close()

        # this allows for the function to open the new tab with the url provided above
        webbrowser.open_new(fileName)



# ends the widget on cancelation
    def cancel(self):
        self.master.destroy()
        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    








