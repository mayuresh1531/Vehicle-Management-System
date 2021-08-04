from tkinter import *
import sqlite3
import sys
import os
from tkinter import messagebox
from tkinter import ttk

root = Tk()

# connect to the databse.
con = sqlite3.connect("v.db")
# cursor to move around the databse
c = con.cursor()


def addv():
                root.destroy()
                os.system('add.py')

def searchv():
                root.destroy()
                os.system('search.py')

def updatev():
                root.destroy()
                os.system('update.py')


def deletev():
                root.destroy()
                os.system('delete.py')
            


class vehiclereg:
        def __init__(self, master):
            self.master = master

            self.x = 0

            # creating the frames in the master
            self.left = Frame(master, width=1366, height=700, bg='skyblue')
            self.left.pack(side=LEFT)

            # heading
            
            self.heading = Label(master, text="Vehicle Management System", font=('arial 40 bold'), fg='green' , bg='skyblue')
            self.heading.place(x=300, y=50)

            # button to home page
            self.submit = Button(text="New Vehicle Registration", width=100, height=2, bg='white', command=addv)
            self.submit.place(x=300, y=150)

            self.submit = Button(text="Search Vehicle Record", width=100, height=2, bg='white',command=searchv)
            self.submit.place(x=300, y=250)

            self.submit = Button(text="Display All Vehicle Records", width=100, height=2, bg='white', command=dispv)
            self.submit.place(x=300, y=350)

            self.submit = Button(text="Update Vehicle Record", width=100, height=2, bg='white', command=updatev)
            self.submit.place(x=300, y=450)

            self.submit = Button(text="Delete Record", width=100, height=2, bg='white', command=deletev)
            self.submit.place(x=300, y=550)

def dispv():
    TABLE_NAME1 = "vehicle"
    
    root.destroy()
    secondWindow = Tk()

    secondWindow.title("Display results")
    appLabel = Label(secondWindow, text="All Vehicle Records",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("#0","one", "two", "three", "four","five")

    tree.heading("#0", text="Vehicle No")
    tree.heading("one", text="Vehicle Model")
    tree.heading("two", text="Yom")
    tree.heading("three", text="Reg Date")
    tree.heading("four", text="Vehicle type")
    tree.heading("five", text="OSSN")
    

    cursor = c.execute("SELECT * FROM " + TABLE_NAME1 + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Vehicle No :" + str(row[0]),
                        values=(row[0],row[1], row[2],
                            row[3], row[4],row[5]))
        i = i + 1

    tree.pack()
    def back():
                
                os.system('vmain.py')

    back = Button(text="Back", width=100, height=2, bg='white', command=back)
    back.place(x=300, y=550)
    # resolution of the window
    secondWindow.geometry("1366x700+0+0")

    # preventing the resize feature
    secondWindow.resizable(False, False)
    secondWindow.mainloop()

root.title("Vehicle Records")
b = vehiclereg(root)

# resolution of the window
root.geometry("1366x700+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
