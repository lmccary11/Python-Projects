from tkinter import *; import tkinter as tk
import file_transfer_main; import file_transfer_func

def load_gui(self):
    #Defining the different components of the tkinter window. Labels, entries and buttons.
    self.btnBrowse1 = tk.Button(self.master, text='Choose Folder to be Checked... ', width= 30, height=1 , font=("Helvitica", 8), fg='black', bg='lightgray', command = lambda: file_transfer_func.browse_src_folder(self))
    self.btnBrowse1.grid(row=0, column=0, padx = (30,0), pady=(30,0))
    self.btnBrowse2 = tk.Button(self.master, text='Choose File Destination Folder... ', width= 30, height=1 , font=("Helvitica", 8), fg='black', bg='lightgray', command = lambda: file_transfer_func.browse_dest_folder(self))
    self.btnBrowse2.grid(row=1, column=0, padx = (30,0), pady=(15,0))
    self.btnCheckforfiles = tk.Button(self.master, text=' Move New Files... ', width= 30, height=2 , font=("Helvitica", 8), fg='black', bg='lightgray', command = lambda: file_transfer_func.checkdates(self))
    self.btnCheckforfiles.grid(row=2, column=0, padx = (30,0), pady=(15,0))
    self.lblDisplay = tk.Label(self.master, text='', font=("Helvitica", 12), fg='black', bg='lightgray')
    self.lblDisplay.grid(row=3, column=1, padx = (30,0), pady=(30,0))
    self.txtSourceFolder = tk.Label(self.master,text=self.varBrowse1, width= 50, font=("Helvitica",12), fg='black', bg='white')
    self.txtSourceFolder.grid(row=0, column=1, columnspan = 2, padx = (30,0), pady=(30,0))
    self.txtDestFolder = tk.Label(self.master,text=self.varBrowse2, width= 50,  font=("Helvitica",12), fg='black', bg='white')
    self.txtDestFolder.grid(row=1, column=1, columnspan = 2, padx=(30,0), pady=(15,0))     
    self.btnSubmit = tk.Button(self.master, text="Close Program", width= 15, height=2, bg='lightgray', command = lambda: file_transfer_func.close(self))
    self.btnSubmit.grid(row=2, column=2, padx=(30,0), pady=(15,0), sticky=NE)  
    


if __name__== "__main__":
    pass
