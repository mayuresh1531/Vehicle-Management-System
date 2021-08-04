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
conn = sqlite3.connect('V.db')
# cursor to move around the databse
c = conn.cursor()

# empty list to later append the ids from the database
ids = []
   
    # tkinter window
class busreport:
        def __init__(self, master):
            self.master = master

            # creating the frames in the master
            self.left = Frame(master, width=1366, height=700)
            self.left.pack(side=LEFT)

            self.right = Frame(master, width=400, height=720, bg='red')
            self.right.pack(side=RIGHT)
            
            # labels for the window
            self.heading = Label(self.left, text="Delete Complaint Details", font=('arial 40 bold'), fg='green',bg='white')
            self.heading.place(x=300, y=50)
        
            self.vno = Label(self.left, text="Enter Vehicle No", font=('arial 15 bold'),fg='black',bg='orange')
            self.vno.place(x=100, y=150)

            
            # Entries for all labels============================================================

            self.vno_ent = Entry(self.left, width=30)
            self.vno_ent.place(x=350, y=150)

           

            # button to perform a command
            self.submit = Button(self.left, text="back", width=20, height=2, command=back)
            self.submit.place(x=150, y=300)

            self.submit = Button(self.left, text="Delete", width=20, height=2, command=self.del_report)
            self.submit.place(x=400, y=300)
            # getting the number of appointments fixed to view in the log
           
            
             # funtion to call when the submit button is clicked
        def del_report(self):
            # getting the user inputs

            self.val1 = self.vno_ent.get()
            
            # checking if the user input is empty
            if self.val1 == '':

                tkMessageBox.showinfo("Warning", "Please Fill Up All Boxes")
            else:
                # now we add to the database
                c.execute("DELETE FROM complaints WHERE vno = ?",(self.val1,))
                conn.commit()
                tkinter.messagebox.showinfo("Success", "Deleted Complaint " +str(self.val1) + " Successfully" )
                

    # creating the object
root = Tk()
root.title("Delete Complaint Details")
b = busreport(root)

      
# resolution of the window
root.geometry("1366x700+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
