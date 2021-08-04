from tkinter import *
import sqlite3
import sys
import os
from tkinter import messagebox
from tkinter import ttk


# connect to the databse.
conn = sqlite3.connect('v.db')
# cursor to move around the databse
c = conn.cursor()

root = Tk()

def addc():
                root.destroy()
                os.system('addc.py')

def searchc():
                root.destroy()
                os.system('searchc.py')
                
def deletec():
                root.destroy()
                os.system('deletec.py')
            


class vehiclereg:
        def __init__(self, master):
            self.master = master

            self.x = 0

            # creating the frames in the master
            self.left = Frame(master, width=1366, height=700, bg='skyblue')
            self.left.pack(side=LEFT)

            # heading
            
            self.heading = Label(master, text="Vehicle Complaints", font=('arial 40 bold'), fg='green' , bg='skyblue')
            self.heading.place(x=470, y=150)

            # button to home page
            self.submit = Button(text="Add Complaint", width=100, height=2, bg='white', command=addc)
            self.submit.place(x=300, y=250)

            self.submit = Button(text="Search Complaint", width=100, height=2, bg='white',command=searchc)
            self.submit.place(x=300, y=350)

            self.submit = Button(text="Display All Vehicle Complaints", width=100, height=2, bg='white', command=dispv)
            self.submit.place(x=300, y=450)

            self.submit = Button(text="Delete Complaint", width=100, height=2, bg='white', command=deletec)
            self.submit.place(x=300, y=550)

def dispv():
    TABLE_NAME1 = "complaints"
    
    root.destroy()
    secondWindow = Tk()

    secondWindow.title("Display results")
    appLabel = Label(secondWindow, text="All Vehicle Records",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("#0","one", "two", "three")

    tree.heading("#0", text="Complaint No")
    tree.heading("one", text="Complaint Desc")
    tree.heading("two", text="Amount of Fine")
    tree.heading("three", text="Vehicle No")
    

    cursor = c.execute("SELECT * FROM " + TABLE_NAME1 + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Complaint No: " + str(row[0]),
                        values=(row[0],row[1], row[2],
                            row[3]))
        i = i + 1

    tree.pack()
    def back():
                
                os.system('vcomplaint.py')

    back = Button(text="Back", width=100, height=2, bg='white', command=back)
    back.place(x=300, y=550)
    # resolution of the window
    secondWindow.geometry("1366x700+0+0")

    # preventing the resize feature
    secondWindow.resizable(False, False)
    secondWindow.mainloop()


root.title("Vehicle Complaint")
b = vehiclereg(root)

# resolution of the window
root.geometry("1366x700+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
