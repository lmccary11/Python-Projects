
import sqlite3 #Accessing database to add text in fileList tuple that ends in .txt (text files)
conn = sqlite3.connect('test.db') #Assigning connection to sqlite to variable conn
with conn:
    cur = conn.cursor() #Using cur to represent cursor method used operate in database
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_filelist TEXT)")
    
    """Creating a table , unless it already existed in db, named tbl_files with
    ID type Integer that autoincrements and contains one named column col_filelist,
    the destination for the text files in the fileList tuple below"""
    
    conn.commit()

conn = sqlite3.connect('test.db')
fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

"""The for loop below extracts the two files that end in .txt and sends them to
the database"""

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_filelist) VALUES(?)", (x,))
            print(x)

conn.close()
        
