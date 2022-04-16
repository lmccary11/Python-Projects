import shutil; import webbrowser;  import os; import datetime; import time#imported to open and remove html file
import tkinter as tk; from tkinter import *; import tkinter.filedialog as fd #imported to run tkinter
import file_transfer_gui; import file_transfer_func

class ParentWindow(Frame): #Initializing Parent Window class for tkinter
    def __init__(self, master):
        Frame.__init__(self)
        #Defining master frame, setting size, title and background color for the tkinter window
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(750, 175))
        #Using CenterWindow method to center app on screen
        #file_transfer_func.center_window(self,600,175)
        self.master.title('Check Files')
        self.master.config(bg='lightgray')
        #This protocol method is a tkinter built-in method to catch if
        #the user clicks the upper corner, "X" on Windows OS.
        #self.master.protocol("WM_DELETE_WINDOW", lambda:file_transfer_func.ask_quit(self))
        #Setting the Web page title and content to string variables and setting instructions
        #for where user will be inputting title and content
        self.varBrowse1 = 'Source'
        self.varBrowse2 = 'Destination'        
        self.varCheckforfiles = StringVar()
        
        self.varCheckforfiles.set('Write some content here')
        #print(self.varFName.get())
        #print(self.varLName.get())
        file_transfer_gui.load_gui(self)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()



