# import modules
from tkinter import *
import sqlite3
import tkinter.messagebox
import sys
import os
root = Tk()
def back():
                root.destroy()
                os.system('vmain.py')

# connect to the databse.
conn = sqlite3.connect('v.db')
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
            self.heading = Label(self.left, text="Update Vehicle Details", font=('arial 40 bold'), fg='red',bg='white')
            self.heading.place(x=300, y=50)
        
            self.vno = Label(self.left, text="Vehicle No", font=('arial 10 bold'),fg='black')
            self.vno.place(x=100, y=150)

            self.vmodel = Label(self.left, text="Vehicle Model", font=('arial 10 bold'), fg='black')
            self.vmodel.place(x=100, y=180)


            self.yom = Label(self.left, text="Year of manfacture", font=('arial 10 bold'), fg='black')
            self.yom.place(x=100, y=210)

            self.regdate = Label(self.left, text="Registration Date", font=('arial 10 bold'), fg='black')
            self.regdate.place(x=100, y=240)


            self.vtype = Label(self.left, text="Vehicle type", font=('arial 10 bold'), fg='black')
            self.vtype.place(x=100, y=270)

            self.ossn= Label(self.left, text="Owner SSN", font=('arial 10 bold'), fg='black')
            self.ossn.place(x=100, y=300)

            self.oname = Label(self.left, text="Owner Name", font=('arial 10 bold'), fg='black')
            self.oname.place(x=100, y=330)

            self.phoneno= Label(self.left, text="Phone No", font=('arial 10 bold'), fg='black')
            self.phoneno.place(x=100, y=360)

            self.address= Label(self.left, text="Address", font=('arial 10 bold'), fg='black')
            self.address.place(x=100, y=390)

            self.lno= Label(self.left, text="License No", font=('arial 10 bold'), fg='black')
            self.lno.place(x=100, y=420)

            self.lclass = Label(self.left, text="License Class", font=('arial 10 bold'), fg='black')
            self.lclass.place(x=100, y=450)

            self.lexp = Label(self.left, text="Licsence Expiry", font=('arial 10 bold'), fg='black')
            self.lexp.place(x=100, y=480)


            # Entries for all labels============================================================

            self.vno_ent = Entry(self.left, width=30)
            self.vno_ent.place(x=350, y=150)

            self.vmodel_ent = Entry(self.left, width=30)
            self.vmodel_ent.place(x=350, y=180)

            self.yom_ent = Entry(self.left, width=30)
            self.yom_ent.place(x=350, y=210)

            self.regdate_ent = Entry(self.left, width=30)
            self.regdate_ent.place(x=350, y=240)

            self.vtype_ent = Entry(self.left, width=30)
            self.vtype_ent.place(x=350, y=270)

            self.ossn_ent = Entry(self.left, width=30)
            self.ossn_ent.place(x=350, y=300)

            self.oname_ent = Entry(self.left, width=30)
            self.oname_ent.place(x=350, y=330)
        
            self.phoneno_ent = Entry(self.left, width=30)
            self.phoneno_ent.place(x=350, y=360)

            self.address_ent = Entry(self.left, width=30)
            self.address_ent.place(x=350, y=390)

            self.lno_ent = Entry(self.left, width=30)
            self.lno_ent.place(x=350, y=420)

            self.lclass_ent = Entry(self.left, width=30)
            self.lclass_ent.place(x=350, y=450)

            self.lexp_ent = Entry(self.left, width=30)
            self.lexp_ent.place(x=350, y=480)

            # button to perform a command
            self.submit = Button(self.left, text="back", width=20, height=2, command=back)
            self.submit.place(x=150, y=520)

            self.submit = Button(self.left, text="Update", width=20, height=2, command=self.add_report)
            self.submit.place(x=400, y=520)
            # getting the number of appointments fixed to view in the log
           
            
             # funtion to call when the submit button is clicked
        def add_report(self):
            # getting the user inputs

            self.val1 = self.vno_ent.get()
            self.val2 = self.vmodel_ent.get()
            self.val3 = self.yom_ent.get()
            self.val4 = self.regdate_ent.get()
            self.val5 = self.vtype_ent.get()
            self.val6 = self.ossn_ent.get()
            self.val7 = self.oname_ent.get()
            self.val8 = self.phoneno_ent.get()
            self.val9 = self.address_ent.get()
            self.val10 = self.lno_ent.get()
            self.val11 = self.lclass_ent.get()
            self.val12 = self.lexp_ent.get()

            # checking if the user input is empty
            if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '':

                tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            else:
                # now we add to the database
                query = "UPDATE license SET lno=?, lclass=?, lexp=? WHERE lno LIKE ?"
                c.execute(query, (self.val10, self.val11, self.val12, self.lno_ent.get(),))
                conn.commit()

                query = "UPDATE owner SET ossn=?, oname=?, phoneno=?, address=?, lno=? WHERE ossn LIKE ?"
                c.execute(query, (self.val6, self.val7, self.val8, self.val9, self.val10,self.ossn_ent.get() ,))
                conn.commit()

                query = "UPDATE vehicle SET vno=?, vmodel=?, yom=?, regdate=?, vtype=?, ossn=? WHERE vno LIKE ?"
                c.execute(query, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6,self.vno_ent.get() ,))
                conn.commit()
                
                tkinter.messagebox.showinfo("Updated", "Successfully Updated.")


                
                
                

    # creating the object

root.title("Update Vehicle Details")
b = busreport(root)

      
# resolution of the window
root.geometry("1366x700+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
