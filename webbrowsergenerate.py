import webbrowser   #imported to open html file
import os           #imported to remove html file before each run of the algorithm
import tkinter      #imported to run tkinter
from tkinter import *

class ParentWindow(Frame): #Initializing Parent Window class for tkinter
    def __init__(self, master):
        Frame.__init__(self)
        #Setting size, title and background color for the tkinter window
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 500))
        self.master.title('Web Page Generator!')
        self.master.config(bg='lightgray')
        #Setting the Web page title and content to string variables and setting instructions
        #for where user will be inputting title and content
        self.varWebTitle = StringVar()
        self.varWebContent = StringVar()
        self.varWebTitle.set('Set Web Page Title')
        self.varWebContent.set('Write some content here')
        #print(self.varFName.get())
        #print(self.varLName.get())

        #Defining the different components of the tkinter window. Labels, entries and buttons.
        self.lblWebTitle = Label(self.master, text='Web Title: ', height=1, font=("Helvitica", 16), fg='black', bg='lightgray' )
        self.lblWebTitle.grid(row=0, column=0, padx = (30,0), pady=(30,0))

        self.lblWebContent = Label(self.master, text='Web Content : ',  height=1, font=("Helvitica", 16), fg='black', bg='lightgray' )
        self.lblWebContent.grid(row=1, column=0, padx = (30,0), pady=(30,0))

        self.lblDisplay = Label(self.master, text='', font=("Helvitica", 16), fg='black', bg='lightgray' )
        self.lblDisplay.grid(row=3, column=1, padx = (30,0), pady=(30,0))

        self.txtWebTitle = Entry(self.master,text=self.varWebTitle, font=("Helvitica",16), fg='black', bg='white')
        self.txtWebTitle.grid(row=0, column=1, padx = (30,0), pady=(30,0))

        self.txtWebContent = Entry(self.master,text=self.varWebContent, font=("Helvitica",16), fg='black', bg='white')
        self.txtWebContent.grid(row=1, column=1, padx=(30,0), pady=(30,0))
        
        self.btnSubmit = Button(self.master, text="Generate Web Page", width= 18, height=2 , command=self.generate)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnSubmit = Button(self.master, text="Cancel", width= 9, height=2 , command=self.cancel)
        self.btnSubmit.grid(row=2, column=1, padx=(0,150), pady=(30,0), sticky=NE)

    #defining method for generate button to generate web page
    def generate(self):
        wt = self.varWebTitle.get()                 #defining varible to get the user's input from tkinter
        wc = self.varWebContent.get()               #defining varible to get the user's input from tkinter        
        self.lblDisplay.config(text='''Your Title is: {} \nYour Content is:{}!'''.format(wt,wc))#displays input on tkinter
        
        os.remove("webbrowsergenerate.html")        #removes previously called html files from folder
        f = open("webbrowsergenerate.html", "x")    #creates html file named 'webbrowsergenerate'
        f = open("webbrowsergenerate.html", "a")    #adds to html file
        #writes code plus user's input from tkinter into html file
        f.write("""
        <html>
        <head>
        <title>{}</title>
        </head>
        <body>
        <h1>
        {}
        </h1>
        </body>
        </html>
        """.format(wt,wc))
        f.close()                                   #closes html file
        file = "webbrowsergenerate.html"            #assigning html file to a variable to use later
        webbrowser.get('windows-default').open_new_tab(file)#opens file in web browser
    #defining method for cancel button to exit tkinter
    def cancel(self):
        self.master.destroy()

        


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

