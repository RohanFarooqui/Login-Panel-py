##Import Goes Here ###
from change_pswd import *
from Scripts.check_name_pswd  import *

from login_check import Login_check
from sign_up     import sign_up
from timer       import timer

import sys
import time
import os
import hashlib
import getpass

### Code start Here ###


def calling_fun(x):
  if(x=="1"):
    os.system('cls')
    Name = str(input("Enter Your Name : "))
    hash1= hashlib.md5(Name.upper().encode())
    hex_dig1 = hash1.hexdigest()

    Pswd = getpass.getpass("Enter your password: ")
    hash2= hashlib.md5(Pswd.encode())
    hex_dig2 = hash2.hexdigest()
    
    Pswd1= getpass.getpass("Re-Enter your password :")
    hash3=hashlib.md5(Pswd1.encode())
    hex_dig3 = hash3.hexdigest()
    
    if(hex_dig2 == hex_dig3):
          check=sign_up(hex_dig1,hex_dig2)
          if(check == True):     print("Signup Sucessfully :) !!")
          elif(check == False):  print("Signup unSucessfully :(  User is Present in our DataBase")
    else:
          print("Input Password not match :(")
  elif(x=="2"):
    os.system('cls')
    x=Login_check()
    if(x == True):
     print("Welcome!! User")
    elif(x == None):
     print("User Not in Database")
  elif(x=="3"):
    os.system('cls')
    change_pswd()
  elif(x=="4"):
      print(" ")
      k=['E','x','i','t','i','n','g',' ','P','r','o','g','r','a','m',' ','.','.','.','.','.',' ','!','!','!','!','!']
      for i in k:
         sys.stdout.write(i)
         sys.stdout.flush()
         time.sleep(.15)
      sys.exit()
         
     
  else:
    print("! Invalid Choice ")



###Main (Calling Functions)
while (True):
 os.system('cls')
 print(" ")
 print("|********Login**Signup******|")
 print("|-----------SYSTEM----------|")
 print("|------Plz Select Option----|")
 print("|> Press 1 to signup        |")
 print("|> Press 2 to Login         |")
 print("|> Press 3 to Change Pswd   |")
 print("|> Press 4 to Exit          |")
 print("|---------------------------|")
 print("|***************************|")
 print(" ")
 x=str(input("Enter Your choice : "))
 calling_fun(x)
   
 



os.system("pause")







### Code End Here ###
