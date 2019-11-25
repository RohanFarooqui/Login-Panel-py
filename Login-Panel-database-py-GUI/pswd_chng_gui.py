#Import Libraries
import os
import hashlib
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import *
from tkinter import messagebox
#Themes Tkinter
from ttkthemes import ThemedStyle

##Import Files
from Scripts.Db_connection import *

#Code Start Here
class Pswd_chng_Window(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
        
    def on_quit(self):
        self.root.destroy()

    def callback(self,event=None):
        w = self.entry1.get()#Name
        x = self.entry2.get()#Current Pswd
        y = self.entry3.get()#New Pswd
        z = self.entry4.get()#Confirm Pswd
        if((len(w) == 0 ) and (len(x) == 0) and (len(y) == 0) and (len(z) == 0)):
              messagebox.showinfo("Error ⚠","Please Enter all Fields !!")
        elif(len(w)== 0):
              messagebox.showinfo("Error ⚠", "Error! Please Input User Name")
        elif(len(x)== 0):
              messagebox.showinfo("Error ⚠", "Error! Please Input Current Password")
        elif(len(y)== 0):
              messagebox.showinfo("Error ⚠", "Error! Please Input New Password")
        elif(len(z)==0):
              messagebox.showinfo("Error ⚠", "Error! Please Confirm Your Password")
        elif((y != z)):
              messagebox.showinfo("Error ⚠", "Error! New Password and Confirm Password not match")
        else:
          if(db_connection == True):
            if(update_pswd(w,x,y) == True):
               messagebox.showinfo("Sucessful", "Password Change Sucessfully !!")
               self.on_quit()
            elif(update_pswd(w,x,y) == False):
               messagebox.showinfo("Error ⚠", "Error! Name is not in Our Database")
               self.entry1.delete(0, END)
               self.entry2.delete(0, END)
               self.entry3.delete(0, END)
               self.entry4.delete(0, END)
            elif(update_pswd(w,x,y) == None):
               messagebox.showinfo("Error ⚠", "Error! Password & Confirm Password not match")
               self.entry2.delete(0, END)
               self.entry3.delete(0, END)
            else:
               messagebox.showinfo("Error ⚠", "Error! Unexpected Error")
          else:
             messagebox.showinfo("Error ⚠", db_connection())
        
    def init_gui(self):
        """Builds GUI."""
        self.root.title('Change Password')
        self.root.wm_iconbitmap('pic/logo.ico')
        self.root.geometry("450x270")
        windowHeight = 270
        windowWidth = 450
        positionRight = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.root.winfo_screenheight()/2 - windowHeight/2)
        self.root.geometry("+{}+{}".format(positionRight, positionDown))
        self.root.resizable(width=False, height=False)
        style = ThemedStyle(self.root)
        style.set_theme("radiance")

       
        #Second Box
        self.root.sec_box = ttk.Frame(self.root,relief=FLAT,borderwidth=1)
        Name = ttk.Label(self.root.sec_box, text="Name :",font = ("Times",13))
        Name.grid(row=1,column=0)
        self.entry1    = ttk.Entry(self.root.sec_box,width="30", justify = CENTER,font = ('Times', 12, 'bold'))
        self.entry1.grid(row=1,column=1,padx=10, pady=10)
        empty_label = ttk.Label(self.root.sec_box,text="").grid(row=2,column=0)
        Pswd = ttk.Label(self.root.sec_box, text=" Current Pswd :",font = ("Times",13))
        Pswd.grid(row=2,column=0)
        self.entry2    = ttk.Entry(self.root.sec_box,width="30",show="*", justify = CENTER,font = ('Times', 12, 'bold'))
        self.entry2.grid(row=2,column=1,padx=10, pady=10)

        Pswd = ttk.Label(self.root.sec_box, text=" New Pswd  :",font = ("Times",13))
        Pswd.grid(row=3,column=0)
        self.entry3    = ttk.Entry(self.root.sec_box,width="30",show="*", justify = CENTER,font = ('Times', 12, 'bold'))
        self.entry3.grid(row=3,column=1,padx=10, pady=10)

        Pswd = ttk.Label(self.root.sec_box, text=" Confirm new Pswd :",font = ("Times",13))
        Pswd.grid(row=4,column=0)
        self.entry4    = ttk.Entry(self.root.sec_box,width="30",show="*", justify = CENTER,font = ('Times', 12, 'bold'))
        self.entry4.grid(row=4,column=1,padx=10, pady=10)
        
        self.root.sec_box.place(relx=0.03, rely=0.02,anchor=NW)

        empty_label = ttk.Label(self.root,text="").grid(row=3,column=0)
        self.button =  ttk.Button(self.root,text=" Change Password ",width="18",command=self.callback).place(relx=0.33, rely=0.72 ,anchor=NW)
        self.button =  ttk.Button(self.root,text=" Close ",width="14",command=self.on_quit).place(relx=0.36, rely=0.86 ,anchor=NW)

        ##KeyBoard Event
        self.root.bind('<Return>', self.callback)
     
        
        



    
