import shutil;  import os; import datetime; import time#imported to open and remove file
import tkinter as tk; from tkinter import *;  import tkinter.filedialog as fd #imported to run tkinter
import file_transfer_gui; import file_transfer_func

 #defining source and destination folders
source = '/Users/User/OneDrive/Desktop/Modified or New/'       
destination = '/Users/User/OneDrive/Desktop/File Destination/'  
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
    
# Round about way of creating and editing random files that will go to "Modified or New" folder and be
# transferred to the "File Destination" folder by the shutil command above
#for demostration purposes
t = datetime.datetime.now() 
mi = t.microsecond;h = t.hour;m = t.minute;s = t.second;x = mi*h;y = mi+m;z = mi-s
fmi = open("/Users/User/OneDrive/Desktop/Modified or New/a{}.txt".format(mi),"x")
fmi = open("/Users/User/OneDrive/Desktop/Modified or New/a{}.txt".format(mi), "a")
fmi.write("New file a{}. Created {}.".format(mi,t));fmi.close()
fx = open("/Users/User/OneDrive/Desktop/Modified or New/e{}.txt".format(x),"x")
fx = open("/Users/User/OneDrive/Desktop/Modified or New/e{}.txt".format(x), "a")
fx.write("New file e{}. Created {}.".format(x,t));fx.close()
fy = open("/Users/User/OneDrive/Desktop/Modified or New/z{}.txt".format(y),"x")
fy = open("/Users/User/OneDrive/Desktop/Modified or New/z{}.txt".format(y), "a")
fy.write("New file z{}. Created {}.".format(y,t));fy.close()
fz = open("/Users/User/OneDrive/Desktop/Modified or New/h{}.txt".format(z),"x")
fz = open("/Users/User/OneDrive/Desktop/Modified or New/h{}.txt".format(z), "a")
fz.write("New file h{}. Created {}.".format(z,t));fz.close()





'''a = "Last modified: %s" % time.localtime(os.path.getmtime("/Users/User/OneDrive/Desktop/Modified or New/{}.txt".format(z)),hour)
b = "Created: %s" % time.localtime(os.path.getctime("/Users/User/OneDrive/Desktop/Modified or New/{}.txt".format(z)),hour)

print(a)
print(b)'''


'''#shutil.move('/Users/User/OneDrive/Documents/GitHub/Python-Projects/{}.txt'.format(x), '/Users/User/OneDrive/Desktop/Modified or New/{}.txt'.format(x))
#source = '/Users/User/OneDrive/Documents/GitHub/Python-Projects/'
#shutil.move('/Users/User/OneDrive/Documents/GitHub/Python-Projects/{}.txt', '/Users/User/OneDrive/Desktop/Modified or New/{}.txt')
#set the destination path to folderB
source = '/Users/User/OneDrive/Desktop/Modified or New/'
destination = '/Users/User/OneDrive/Desktop/File Destination/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their destination
    shutil.move(source+i, destination)

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() '''
