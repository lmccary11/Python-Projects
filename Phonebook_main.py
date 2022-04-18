from tkinter import *
import tkinter as tk

import Phonebook_gui #referencing the phonebook files where the user interface is developed
import Phonebook_func #referencing the phonebook file that holds the functions needed to access db and other events

#classifying and initializing the main window
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)         
        Phonebook_func.center_window(self,500,300)
        self.master.title('Phonebook Demo')
        self.master.configure(bg='lightgray')
        #Built in tkinter method to confirm the user wants to quit if X in the upper right corner is clicked
        self.master.protocol("WM_DELETE_WINDOW", lambda: Phonebook_func.ask_quit(self))
        arg = self.master

        #load the Interface in a seperate file
        Phonebook_gui.load_gui(self)

if __name__=="__main__":
    root = tk=Tk()
    App = ParentWindow(root)
    root.mainloop()
        

