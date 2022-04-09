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

#inputting values into column.
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_submission(col_file) VALUES (?)", \
                ('Hello.txt',))
    cur.execute("INSERT INTO tbl_submission(col_file) VALUES (?)", \
                ('World.txt',))
    conn.commit()
conn.close()

# calling another connection for changes to be made 
conn = sqlite3.connect('submission.db')


with conn:
    cur = conn.cursor()
    cur.execute(" SELECT * FROM tbl_submission")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File Name: {}".format(item[1])
        print(msg)




    
                




            
