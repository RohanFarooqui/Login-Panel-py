#Import Libraries
import os
import hashlib
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import *
from tkinter import messagebox
##Import Files
from Scripts.signup_code import sign_up
from Scripts.side_function import *

#etc
from ttkthemes import ThemedStyle

#Code Start Here
class Sign_up(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
        
    def on_quit(self):
        self.root.destroy()

    def callback(self,event=None):
        x = self.entry1.get()
        y = self.entry2.get()
        z = self.entry3.get()
        if((len(x) == 0 ) and (len(y) == 0)and (len(z) == 0)):
              messagebox.showinfo("Error ⚠","Please Enter User Name && Password && Confirm Your Password !!")
        elif(len(x)== 0):
              messagebox.showinfo("Error ⚠", "Error! Please Input User Name")
        elif(len(y)== 0):
              messagebox.showinfo("Error ⚠", "Error! Please Input Password")
        elif(len(z)==0):
              messagebox.showinfo("Error ⚠", "Error! Please Confirm Your Password")
        #elif(y != z):
              #messagebox.showinfo("Error ⚠", "Error! Password & Confirm Password not match")
              #self.entry3.delete(0, END)
              #self.entry2.delete(0, END)
        else:
            Name = remove_space(x)
            hash1= hashlib.md5(Name.upper().encode())
            hex_dig1 = hash1.hexdigest()
            Pswd = y
            hash2= hashlib.md5(Pswd.encode())
            hex_dig2 = hash2.hexdigest()
            Pswd1= z
            hash3=hashlib.md5(Pswd1.encode())
            hex_dig3 = hash3.hexdigest()
            if(hex_dig2 == hex_dig3):
                  check= sign_up(hex_dig1,hex_dig2)
                  if(check == True):
                      messagebox.showinfo("Sucess", "Account is Created Sucesfully :)")
                      self.root.destroy()
                  elif(check == False):
                      messagebox.showinfo("UnSucess", "Error! User is Present in our Database")
                      self.entry3.delete(0, END)
                      self.entry2.delete(0, END)
                      self.entry1.delete(0, END)
                      
                      
            else:
                check= sign_up(hex_dig1,hex_dig2)
                if(check == False):
                      messagebox.showinfo("UnSucess", "Error! User is Present in our Database")
                      self.entry3.delete(0, END)
                      self.entry2.delete(0, END)
                      self.entry1.delete(0, END)
                else:
                      messagebox.showinfo("Error ⚠", "Error! Password & Confirm Password not match :(")
                      self.entry3.delete(0, END)
                      self.entry2.delete(0, END)

    def init_gui(self):
        """Builds GUI."""
        self.root.title('Change Password')
        self.root.wm_iconbitmap('pic/logo.ico')
        self.root.geometry("450x230")
        windowHeight = 230
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
        #empty_label = Label(self.root.sec_box,text="").grid(row=2,column=0)
        

        Pswd = ttk.Label(self.root.sec_box, text=" Enter Password  :",font = ("Times",13))
        Pswd.grid(row=3,column=0)
        self.entry2    = ttk.Entry(self.root.sec_box,width="30",show="*", justify = CENTER,font = ('Times', 12, 'bold'))
        self.entry2.grid(row=3,column=1,padx=10, pady=10)

        Pswd = ttk.Label(self.root.sec_box, text=" Confirm Password :",font = ("Times",13))
        Pswd.grid(row=4,column=0)
        self.entry3    = ttk.Entry(self.root.sec_box,width="30",show="*", justify = CENTER,font = ('Times', 12, 'bold'))
        self.entry3.grid(row=4,column=1,padx=10, pady=10)
        
        self.root.sec_box.place(relx=0.03, rely=0.02,anchor=NW)

        empty_label = ttk.Label(self.root,text="").grid(row=3,column=0)
        self.button =  ttk.Button(self.root,text=" Signup ",width="14",command=self.callback).place(relx=0.36, rely=0.66 ,anchor=NW)
        self.button =  ttk.Button(self.root,text=" Close ",width="14",command= self.on_quit).place(relx=0.36, rely=0.83 ,anchor=NW)

        ##KeyBoard Event
        self.root.bind('<Return>', self.callback)
        
        



if __name__ == '__main__':
    root = Tk()
    Sign_up(root)
    root.mainloop()
