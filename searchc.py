from tkinter import *
import sqlite3
import sys
import os
from tkinter import messagebox


conn = sqlite3.connect('v.db')
c = conn.cursor()

root = Tk()

def back():
                root.destroy()
                os.system('vcomplaint.py')

class update(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

       

        self.heading = Label(master, text="Search Complaint Details",  fg='green',bg='white' , font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        # search criteria name 
        self.vno = Label(master, text="Enter Vehicle No",bg='orange' , font=('arial 18 bold'))
        self.vno.place(x=0, y=100)

        # entry for  the name
        self.vno = Entry(master, width=30)
        self.vno.place(x=280, y=102)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='white', command=self.search_db)
        self.search.place(x=350, y=142)

        self.search = Button(master, text="Back", width=12, height=1, bg='white', command=back)
        self.search.place(x=550, y=142)
        
    # function to search
    def search_db(self):
        self.input = self.vno.get()
        # execute sql 

        sql = "SELECT * FROM complaints WHERE vno LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.Name = self.row[0]
            self.busNo = self.row[1]
            self.source = self.row[2]
            self.dest = self.row[3]
           
        # creating the update form

        self.uName = Label(self.master, text="Complaint No",bg='orange' , font=('arial 18 bold'))
        self.uName.place(x=0, y=220)

        self.ubusNo = Label(self.master, text="Complaint Description",bg='orange' , font=('arial 18 bold'))
        self.ubusNo.place(x=0, y=260)

        self.usource = Label(self.master, text="Amount of Fine",bg='orange' , font=('arial 18 bold'))
        self.usource.place(x=0, y=300)

        self.udest = Label(self.master, text="Vehicle No",bg='orange' , font=('arial 18 bold'))
        self.udest.place(x=0, y=340)

        
        # filling the search result in the entry box to update

        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=220)
        self.ent1.insert(END, str(self.Name))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=260)
        self.ent2.insert(END, str(self.busNo))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=300)
        self.ent3.insert(END, str(self.source))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=340)
        self.ent4.insert(END, str(self.dest))

        
root.title("Search")
b = update(root)
root.geometry("1366x700+0+0")
root.resizable(False, False)
root.mainloop()
