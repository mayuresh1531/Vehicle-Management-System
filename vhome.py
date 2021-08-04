from tkinter import *
import sys
import os
from tkinter import ttk
from tkinter import messagebox

# pip install pillow
from PIL import Image, ImageTk

def ecomplaints():
                os.system('vcomplaint.py')

def vehiclereg():
                os.system('vmain.py')

class Window(Frame):
    def __init__(self, master):

            Frame.__init__(self, master)
            self.master = master
            self.pack(fill=BOTH, expand=1)

            
            load = Image.open("v2.jpg")
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=0, y=0)

            self.new = Frame(bg='skyblue')

            self.heading = Label(text="Vehicle Management System", font=('times 40 bold'), fg='lightslateblue' )
            self.heading.place(x=350, y=100)

            # button to home page
            self.submit = Button(text="Home", width=25, height=2, bg='white')
            self.submit.place(x=415, y=200)
            
            self.submit = Button(text="Vehicle Registration", width=25, height=2, bg='white',command=vehiclereg)
            self.submit.place(x=600, y=200)

            self.submit = Button(text="E-Complaints", width=25, height=2, bg='white',command=ecomplaints)
            self.submit.place(x=780, y=200)

        
root = Tk()
app = Window(root)
root.wm_title("VEHICLE MANAGEMENT SYSTEM")

# resolution of the window
root.geometry("1366x700+0+0")
'''
# preventing the resize feature
root.resizable(False, False)
'''
# end the loop
root.mainloop()
