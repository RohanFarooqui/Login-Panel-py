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
from Scripts.side_function import *
from Scripts.Db_connection import *

##GUI files
from pswd_chng_gui import *
from sign_up_gui import *
##Other Imp
import webbrowser


#Code Start Here
click = 0
check = 3

class Main_Window(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    ##URL Links Binding
    def feedback(self):
         webbrowser.open_new("https://drive.google.com/open?id=16TRryXb7NgI2qYuMM5phNpDqJDTdivXaBJsk5ffDNZM")

    def github(self):
         webbrowser.open_new("http://www.github.com/LOL-32")

    def website(self):
         webbrowser.open_new("http://www.rohanfarooqui.wordpress.com")

    ##Functions
    def on_quit(self,event):
        self.root.destroy()
           
    def forgot_pass(self, event):
           self.forgot_window = Tk()
           Pswd_chng_Window(self.forgot_window)

    def sign_up(self,event):
           self.signup_window = Tk()
           Sign_up(self.signup_window)

   
    def countdown(self,x):
           while(x>0): 
               self.timer.configure(text="Timer : {0}  ".format(x))
               time.sleep(0.1)
               x= x-1
               self.root.update()    

    def entry_normal(self):
          self.entry1.configure(state='normal')
          self.entry2.configure(state='normal')
          self.button_1.configure(state="normal")
          self.timer.configure(text="")
          self.remain.configure(text="3")
          
    def callback(self,event=None):
        if(db_connection == True):
          global click
          global check
          click = click + 1
          x = remove_space(self.entry1.get())
          y = self.entry2.get()
          if((len(x) == 0 ) and (len(y) == 0)):
              messagebox.showinfo("Error ⚠","Please Enter User Name && Password !!")
              click = click - 1
          elif(len(y) == 0):
               messagebox.showinfo("Error ⚠","Please Enter Password !!")
               click = click -1
          elif(len(x) == 0 ):
                messagebox.showinfo("Error ⚠","Please Enter User Name !!")
                click = click - 1
          elif(login_check(x,y) == True):
             message ="Welcome :"+x
             messagebox.showinfo("Sucess!!",message )
             self.entry1.delete(0, END)
             self.entry2.delete(0, END)
          elif(login_check(x,y) == None):
             messagebox.showinfo("Error ⚠", "Error! User not in our Database")
          elif(login_check(x,y) == False):
             if(click == 3):
                 click = 0
                 check = 3
                 self.remain.configure(text="0")
                 messagebox.showinfo("Error ⚠", "Max tries Limit i.e 3 reached, Try Again after 1 minute")
                 self.entry1.configure(state='disabled')
                 self.entry2.configure(state='disabled')
                 self.button_1.config(state = 'disabled')
                 self.countdown(10)
                 self.root.after(100, self.entry_normal)#10000  
             else:
                 check = check - 1
                 self.remain.configure(text="{0}  ".format(check))
                 self.root.update()
                 self.entry2.delete(0, END)
          else:
             messagebox.showinfo("Error ⚠", "Error! Unexpected Error")
        else:
            messagebox.showinfo("Error ⚠", db_connection())
         
    
    def init_gui(self):
        """Builds GUI."""
        self.root.title('Login Panel')
        try:
           self.root.iconbitmap('pic/logo.ico')
        except:
            pass           
        self.root.geometry("350x465")
        windowHeight = 350
        windowWidth = 350
        positionRight = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.root.winfo_screenheight()/2 - windowHeight/2)
        self.root.geometry("+{}+{}".format(positionRight, positionDown))
        self.root.resizable(width=False, height=False)
        style = ThemedStyle(self.root)
        style.set_theme("radiance")

        #Menu bar
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label=" Google-Feedback",font=("Times",10),command=self.feedback)
        editmenu.add_command(label=" Github Code-link",font=("Times",10),command=self.github) 
        editmenu.add_command(label=" My Website",font=("Times",10),command=self.website)
        menubar.add_cascade(label="Feed Back // Code Link", menu=editmenu)

        self.root.config(menu=menubar)
        
        
        #First Box
        self.root.first_box = ttk.Frame(self.root,relief=FLAT,borderwidth=0)

        empty = ttk.Label(self.root.first_box,text="").grid(row=0,column=1)
        heading = ttk.Label(self.root.first_box, text="Login Panel ",font = ("Times",20))
        heading.grid(row=0,column=2,columnspan=4)
        self.root.logo_1 =PhotoImage(file = 'pic/180x180.png')
        label = tk.Label(self.root.first_box,image=self.root.logo_1,width="180",height="180")
        label.grid(row=1, column=2,columnspan=4)
        label.image = self.root.logo_1
        copyright_symbol = ttk.Label(self.root.first_box,text="M.ROHAN FAROOQUI © 2019").grid(row=2,column=2,columnspan=4)
        self.root.first_box.place(relx=0.21, rely=0.009,anchor=NW)

        
        #Second Box
        self.root.sec_box = ttk.Frame(self.root,relief=FLAT,borderwidth=0)
        Name = ttk.Label(self.root.sec_box, text="Name :",font = ("Times",13))
        Name.grid(row=1,column=0)
        self.entry1    = ttk.Entry(self.root.sec_box,width="30", justify = CENTER,font = ('Times', 12, 'bold'))
        self.entry1.grid(row=1,column=1,padx=10, pady=10)
        empty_label = ttk.Label(self.root.sec_box,text="").grid(row=2,column=0)
        Pswd = ttk.Label(self.root.sec_box, text="Pswd :",font = ("Times",13))
        Pswd.grid(row=2,column=0)
        self.entry2    = ttk.Entry(self.root.sec_box,width="30",show="*", justify = CENTER,font = ('Times', 12, 'bold'))
        self.entry2.grid(row=2,column=1,padx=10, pady=10)
        self.root.sec_box.place(relx=0.03, rely=0.57,anchor=NW)

        ##Login_button label
        self.button_1=  ttk.Button(self.root,text=" Login ",width="10",command=self.callback)
        self.button_1.place(relx=0.35, rely=0.81,anchor=NW)

        ##Forgot Label
        self.link_1 = ttk.Label(self.root, text=" Forgot Pswd ? ", cursor="hand2",font=("Times",9,'bold'))
        f = font.Font(self.link_1, self.link_1.cget("font"))
        f.configure(underline=True)
        self.link_1.bind("<Button-1>",  self.forgot_pass)
        self.link_1.configure(font=f)
        self.link_1.place(relx=0.76, rely=0.8,anchor=NW)
        
        ##Signup Label
        self.link_2 = ttk.Label(self.root, text=" or  Sign up ", cursor="hand2",font=("Times",9,'bold'))
        f = font.Font(self.link_1, self.link_1.cget("font"))
        f.configure(underline=True)
        self.link_2.configure(font=f)
        self.link_2.bind("<Button-1>",  self.sign_up)
        self.link_2.place(relx=0.79, rely=0.87,anchor=NW)

        ##Attempt label
        self.attempt = ttk.Label(self.root,text="Attempt Remaining : ")
        self.attempt.place(relx=0.02, rely=0.91,anchor=NW)
        self.remain = ttk.Label(self.root,text="3")
        self.remain.place(relx=0.41, rely=0.91,anchor=NW)

        ##Timer Label
        self.timer = ttk.Label(self.root, text="")
        self.timer.place(relx=0.02,rely=0.95,anchor=NW)

        ##Version Label
        version_label = ttk.Label(self.root,text="V 1.0",font =("Times",10)).place(relx=0.88, rely=0.95,anchor=NW)

        ##KeyBoard Event
        self.root.bind('<Return>', self.callback)
        
        
        
        
        
if __name__ == '__main__':
    root = Tk()
    Main_Window(root)
    root.mainloop()
