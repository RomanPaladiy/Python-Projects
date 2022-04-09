# importing sqlite so I can  use it's functionality
import sqlite3

# naming a database and creating it using .connect
conn = sqlite3.connect('submission.db')

# here the table is created with a primary key and a string 
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_submission( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
# using the commit function to make the changes/creation of table
    conn.commit()
conn.close()


#restating that I am making another connection to the db to input values
conn = sqlite3.connect('submission.db')


# this is the list of files to be parsed through

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


# this is a loop through each object in the tuple to find the file names that end in .txt.
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_submission(col_file) VALUES (?)",(x,))
            print(x)

conn.close()
        





    
                




            
