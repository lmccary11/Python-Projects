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
        modified_time = (os.path.getmtime('/Users/User/OneDrive/Desktop/Modified or New/{}'.format(i)))
        created_time = (os.path.getctime('/Users/User/OneDrive/Desktop/Modified or New/{}'.format(i)))
        #string decribing when file " i " in the folder was modified, created
        a = "Last modified: %s" % time.ctime(modified_time)
        b = "Created: %s" % time.ctime(created_time)
        #integer decribing when file " i " in the folder was modified, created
        f = (int(modified_time))
        e = (int(created_time))
        #Determining whether to use modified_time or created_time based on whether or not file has been modified
        if f == e:
            d=f
        if  f != e:
            d=e
        #getting current time since epoch (seconds) and subtracting modified/created time of files (seconds) to get
        #time since creation/modification in seconds, "sime_since_modcreation"
        date_time = int(time.time())
        time_since_modcreation = date_time - d                
        print(i + '\n' + b + ' || ' +a + '\n' +'{} - {} = {}.        {} Was made/edited {} Seconds Ago.'.format(date_time,d,time_since_modcreation,i,time_since_modcreation))
        #setting condition to move files that have been created or modified within the last day (86400 seconds)
        if (time_since_modcreation) > 86400: 
            print('{} has been modified or created more than a day ago.'.format(i))
            print('{}  > 86400.'.format(time_since_modcreation))
            print(' NOT MOVED: REMAINS IN MODIIFIED OR NEW\n- - - - - - - - - -\n\n')
            continue # using continue to move on to next item " i " in file if condition is satisfied
        print(' MOVED: SENT TO FILE DESTINATION\n- - - - - - - - - -\n\n')
        #moving files that did not satisfy the if condition immediately above
        shutil.move(source+i, destination)
        #shutil.copy(source+i, destination)
    
def close(self):
    self.master.destroy()
    
    
    
