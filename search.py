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
                os.system('vmain.py')

class update(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

            
       
        self.heading = Label(master, text="Search Vehicle Details",  fg='red',bg='white' , font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        # search criteria name 
        self.vno = Label(master, text="Enter  Vehicle No: ",bg='orange' , font=('arial 18 bold'))
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

        sql = "SELECT * FROM vehicle WHERE vno LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.vno = self.row[0]
            self.vmodel = self.row[1]
            self.yom = self.row[2]
            self.regdate = self.row[3]
            self.vtype = self.row[4]
            self.ossn2 = self.row[5]

        self.input2 = self.vno
        # execute sql 

        sql2 = "SELECT * FROM owner WHERE ossn IN(SELECT o.ossn FROM vehicle v,owner o where o.ossn=v.ossn AND v.vno= ? )"
        self.res2 = c.execute(sql2, (self.input2,))
        for self.row in self.res:
            self.oname = self.row[1]
            self.ph = self.row[2]
            self.address = self.row[3]
            self.lno = self.row[4]

        sql3 = "SELECT * FROM license WHERE lno IN(SELECT o.lno FROM vehicle v,owner o,license l WHERE o.ossn=v.ossn AND o.lno=l.lno AND v.vno= ?)"
        self.res3 = c.execute(sql3, (self.input2,))
        for self.row in self.res3:
            self.lclass = self.row[1]
            self.lexp = self.row[2]
            
        # creating the update form

        self.uName = Label(self.master, text="Vehicle No : ",bg='skyblue' , font=('arial 10 bold'))
        self.uName.place(x=0, y=220)

        self.ubusNo = Label(self.master, text="Vehicle Model : ",bg='skyblue' , font=('arial 10 bold'))
        self.ubusNo.place(x=0, y=250)

        self.usource = Label(self.master, text="Year of Manufacture : ",bg='skyblue' , font=('arial 10 bold'))
        self.usource.place(x=0, y=280)

        self.udest = Label(self.master, text="Registration Date : ",bg='skyblue' , font=('arial 10 bold'))
        self.udest.place(x=0, y=310)

        self.uDistance = Label(self.master, text="Vehicle Type : ",bg='skyblue' , font=('arial 10 bold'))
        self.uDistance.place(x=0, y=340)

        self.ossn= Label(self.master, text="Owner SSN : ",bg='skyblue' , font=('arial 10 bold'))
        self.ossn.place(x=0, y=370)

        self.uType = Label(self.master, text="Owner Name : ",bg='skyblue' , font=('arial 10 bold'))
        self.uType.place(x=0, y=400)

        self.uType = Label(self.master, text="Phone No : ",bg='skyblue' , font=('arial 10 bold'))
        self.uType.place(x=0, y=430)

        self.uType = Label(self.master, text="Address : ",bg='skyblue' , font=('arial 10 bold'))
        self.uType.place(x=0, y=460)

        self.uType = Label(self.master, text="License No : ",bg='skyblue' , font=('arial 10 bold'))
        self.uType.place(x=0, y=490)

        self.uType = Label(self.master, text="License Class : ",bg='skyblue' , font=('arial 10 bold'))
        self.uType.place(x=0, y=520)

        self.uType = Label(self.master, text="License expiry : ",bg='skyblue' , font=('arial 10 bold'))
        self.uType.place(x=0, y=550)



        # filling the search result in the entry box to update

        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=220)
        self.ent1.insert(END, str(self.vno))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=250)
        self.ent2.insert(END, str(self.vmodel))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=280)
        self.ent3.insert(END, str(self.yom))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=310)
        self.ent4.insert(END, str(self.regdate))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=340)
        self.ent5.insert(END, str(self.vtype))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=370)
        self.ent6.insert(END, str(self.ossn2))


        self.ent7 = Entry(self.master, width=30)
        self.ent7.place(x=300, y=400)
        self.ent7.insert(END, str(self.oname))

        self.ent8 = Entry(self.master, width=30)
        self.ent8.place(x=300, y=430)
        self.ent8.insert(END, str(self.ph))

        self.ent9 = Entry(self.master, width=30)
        self.ent9.place(x=300, y=460)
        self.ent9.insert(END, str(self.address))

        self.ent10 = Entry(self.master, width=30)
        self.ent10.place(x=300, y=490)
        self.ent10.insert(END, str(self.lno))

        self.ent11 = Entry(self.master, width=30)
        self.ent11.place(x=300, y=520)
        self.ent11.insert(END, str(self.lclass))

        self.ent12 = Entry(self.master, width=30)
        self.ent12.place(x=300, y=550)
        self.ent12.insert(END, str(self.lexp))



 
b = update(root)
root.geometry("1366x700+0+0")
root.resizable(False, False)
root.mainloop()
