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
class vehiclereg:
        def __init__(self, master):
            self.master = master

            # creating the frames in the master
            self.left = Frame(master, width=1366, height=700)
            self.left.pack(side=LEFT)

            self.right = Frame(master, width=400, height=720, bg='red')
            self.right.pack(side=RIGHT)
            
            # labels for the window
            self.heading = Label(self.left, text="Delete Vehicle Record", font=('arial 40 bold'), fg='red',bg='white')
            self.heading.place(x=300, y=50)
        
            self.vno = Label(self.left, text="Enter Vehicle No", font=('arial 15 bold'),fg='black',bg='orange')
            self.vno.place(x=100, y=150)

            
            # Entries for all labels============================================================

            self.vno_ent = Entry(self.left, width=30)
            self.vno_ent.place(x=350, y=150)

           

            # button to perform a command
            self.submit = Button(self.left, text="back", width=20, height=2, command=back)
            self.submit.place(x=150, y=300)

            self.submit = Button(self.left, text="Delete", width=20, height=2, command=self.deletev)
            self.submit.place(x=400, y=300)
            # getting the number of appointments fixed to view in the log
           
            
             # funtion to call when the submit button is clicked
        def deletev(self):
            # getting the user inputs

            self.valdel = self.vno_ent.get()
            

            # checking if the user input is empty
            if self.valdel == '' :

                tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            else:
                # now we add to the database
                query = "DELETE FROM vehicle WHERE vehicle.vno = ? "
                c.execute(query, (self.valdel,))
                conn.commit()
                tkinter.messagebox.showinfo("Success", "Deleted Records for " +str(self.valdel) + " " )
                

    # creating the object

root.title("Delete Vehicle Record")
b = vehiclereg(root)

      
# resolution of the window
root.geometry("1366x700+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
