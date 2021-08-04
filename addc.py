# import modules
from tkinter import *
import sqlite3
import tkinter.messagebox
import sys
import os

def back():
                root.destroy()
                os.system('vcomplaint.py')

# connect to the databse.
conn = sqlite3.connect('v.db')
# cursor to move around the databse
c = conn.cursor()

# empty list to later append the ids from the database
ids = []

#Creating Tables

c.execute("CREATE TABLE IF NOT EXISTS complaints (cno INTEGER PRIMARY KEY, cname TEXT, "
                    "amt INTEGER,vno INTEGER,FOREIGN KEY(vno) REFERENCES vehicle(vno) ON DELETE CASCADE ON UPDATE CASCADE)")
                
conn.commit()
   
# tkinter window
class complaint:
        def __init__(self, master):
            self.master = master

            # creating the frames in the master
            self.left = Frame(master, width=1366, height=700)
            self.left.pack(side=LEFT)

            self.right = Frame(master, width=400, height=720, bg='red')
            self.right.pack(side=RIGHT)
            
            # labels for the window
            self.heading = Label(self.left, text="Enter Complaint Details", font=('arial 40 bold'), fg='green',bg='white')
            self.heading.place(x=300, y=50)
        
            self.cno = Label(self.left, text="Complaint No", font=('arial 10 bold'),fg='black')
            self.cno.place(x=100, y=150)

            self.cvno = Label(self.left, text="Vehicle No", font=('arial 10 bold'),fg='black')
            self.cvno.place(x=100, y=180)

            self.cname = Label(self.left, text="Complaint description", font=('arial 10 bold'), fg='black')
            self.cname.place(x=100, y=210)


            self.amt = Label(self.left, text="Amount of Fine", font=('arial 10 bold'), fg='black')
            self.amt.place(x=100, y=240)

            
            # Entries for all labels============================================================

            self.cno_ent = Entry(self.left, width=30)
            self.cno_ent.place(x=350, y=150)
            
            self.cvno_ent = Entry(self.left, width=30)
            self.cvno_ent.place(x=350, y=180)

            self.cname_ent = Entry(self.left, width=30)
            self.cname_ent.place(x=350, y=210)

            self.amt_ent = Entry(self.left, width=30)
            self.amt_ent.place(x=350, y=240)


            # button to perform a command
            self.submit = Button(self.left, text="back", width=20, height=2, command=back)
            self.submit.place(x=150, y=520)

            self.submit = Button(self.left, text="Submit", width=20, height=2, command=self.add_report)
            self.submit.place(x=400, y=520)
            # getting the number of appointments fixed to view in the log
           
            
             # funtion to call when the submit button is clicked
        def add_report(self):
            # getting the user inputs

            self.val1= self.cno_ent.get()
            self.val4 = self.cvno_ent.get()
            self.val2 = self.cname_ent.get()
            self.val3 = self.amt_ent.get()

            # checking if the user input is empty
            if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' :

                tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            else:
                # now we add to the database
                
                sql4 = "INSERT INTO 'Complaints'(cno, cname, amt, vno) VALUES(?, ?, ?, ?)"
                c.execute(sql4, (self.val1, self.val2, self.val3, self.val4))
                conn.commit()
               
                tkinter.messagebox.showinfo("Success", "Added complaint to  " +str(self.val4) + " Vehicle" )
                

    # creating the object
root = Tk()
root.title("Complaint Details")
b = complaint(root)

      
# resolution of the window
root.geometry("1366x700+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
