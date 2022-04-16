import shutil; import webbrowser;  import os; import datetime; import time#imported to open and remove html file
import tkinter as tk; from tkinter import *;  import tkinter.filedialog as fd #imported to run tkinter
import file_transfer_gui; import file_transfer_main

def browse_src_folder(self):    
    selected_src_folder = fd.askdirectory()
    print(selected_src_folder)
    self.txtSourceFolder.config(text=selected_src_folder)
    self.varBrowse1=selected_src_folder       
    
def browse_dest_folder(self):
    selected_dest_folder = fd.askdirectory()
    print(selected_dest_folder)
    self.txtDestFolder.config(text=selected_dest_folder)
    self.varBrowse2=selected_dest_folder    

def checkdates(self):
    #defining source and destination folders
    source = '{}/'.format(self.varBrowse1)
    print(source)
    destination =  '{}/'.format(self.varBrowse2)
    print(destination)
    files = os.listdir(source)  #defining "files" as the directory list of files in the source folder 
    # for loop function that will execute following script for each item or file " i " in the directory list of files in the source folder 
    for i in files:
        modified_time = (os.path.getmtime(source+i))
        created_time = (os.path.getctime(source+i))
        #string decribing when file " i " in the folder was modified, created
        a = "Last modified: %s" % time.ctime(modified_time)
        b = "Created: %s" % time.ctime(created_time)
        #integer decribing when file " i " in the folder was modified, created
        f = (int(modified_time))
        e = (int(created_time))
        #Determining whether to use modified_time or created_time based on whether or not file has been modified
        if f == e:
            d=f
        elif  f != e:
            d=e
        #getting current time since epoch (seconds) and subtracting modified/created time of files (seconds) to get
        #time since creation/modification in seconds, "sime_since_modcreation"
        date_time = int(time.time())
        time_since_modcreation = date_time - d
        modTime = datetime.datetime.fromtimestamp(modified_time)
        twentyFour = datetime.datetime.now() - datetime.timedelta(hours=24)
        print(i + '\n' + b + ' || ' +a + '\n')
        #setting condition to move files that have been created or modified within the last day
        if (modTime > twentyFour):
            print(' MOVED: SENT TO FILE DESTINATION\n- - - - - - - - - -\n\n')
            #moving files that were modified in the last 24 hours
            shutil.move(source+i, destination)            
            continue # using continue to move on to next item " i " in file if condition is satisfied
        else:
            print('{} has been modified or created more than a day ago.'.format(i))            
            print(' NOT MOVED: REMAINS IN MODIIFIED OR NEW\n- - - - - - - - - -\n\n')               
           
def close(self):
    self.master.destroy()
    
    
    
