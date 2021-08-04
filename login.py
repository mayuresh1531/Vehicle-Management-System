from tkinter import *
import sqlite3
import sys
import os
import tkinter.messagebox


# pip install pillow
from PIL import Image, ImageTk

root = Tk()
root.title("Login")


name_inp = StringVar()
password_inp = StringVar()



def enter():
	if name_inp.get() == "prathamesh" and password_inp.get() == "prathamesh":
		root.destroy()
		import vhome
	else:
		tkinter.messagebox.showinfo('Error','Username and Password is incorrect')
		name_inp.set("")
		password_inp.set("")	

def exit():
	root.destroy()


class login(Frame):
        def __init__(self, master):
            
            Frame.__init__(self, master,bg='lightsteelblue')
            self.master = master
            self.pack(fill=BOTH, expand=1)

            
            load = Image.open("11.jpg")
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=500, y=200)

            

            # heading
            self.heading = Label(master, text="VEHICLE MANAGEMENT SYSYTEM", font=('Sylfaen 50'),fg="#06a099",bg='white')
            self.heading.place(x=100, y=0)
            
            self.heading = Label(master, text="Login to your account", font=('arial 30 bold'))
            self.heading.place(x=0, y=250)

            self.heading = Label(master, text="Project by:Prathamesh,Vicky,Rutwik", font=('arial 30 bold'))
            self.heading.place(x=0, y=650)

            # button to home page

            self.username = Label(self, text="Username", font=('arial 18 bold'))
            self.username.place(x=0, y=400)

            self.password = Label(self, text="Password", font=('arial 18 bold'))
            self.password.place(x=0, y=440)

            self.username = Entry(self, textvariable = name_inp, width=30)
            self.username.place(x=250, y=400)

            self.password = Entry(self, textvariable = password_inp, width=30, show="*")
            self.password.place(x=250, y=440)

            self.login = Button(text="Sign In", width=25, height=2,command=enter)
            self.login.place(x=150, y=500)

            exit_btn = Button(text="Exit", width=25, height=2,command=exit)
            exit_btn.place(x=500,y=500)


b = login(root)
# resolution of the window
root.geometry("1366x700+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
