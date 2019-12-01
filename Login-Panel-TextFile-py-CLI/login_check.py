##Import Goes Here ###
##Import Libraries 
import os
import hashlib
import getpass
from timer import timer
import time

##Import Files
from timer import *


### Code start Here ###
def Login_check():
 n = 3
 Name = str(input("                            Enter Your Name : "))
 Name1= Name.upper()
 hash1= hashlib.md5(Name1.encode())
 hex_dig1 = hash1.hexdigest()
 while(n > 0):
     Pswd = getpass.getpass("                            Enter your password: ")
     hash2= hashlib.md5(Pswd.encode())
     hex_dig2 = hash2.hexdigest()
     file = open("login.txt","r")
     lis=[]
     for i in file:
       k=(i.split(' '))
       lis.append(k[0])
       lis.append(k[1])
       lis[-1] = lis[-1].strip()
     for i in range(0,len(lis)):
      if(lis[i] == hex_dig1):
         if(lis[i+1] == hex_dig2):
           return True
         elif(lis[i+1] != hex_dig2):
           n=n-1
           if(n > 0):
             print("                      ",n,"Tries Left, Total Tries are '3' ")            
           else:
             print("                     Max tries Limit i.e 3 reached, Try Again")
             timer(5)
             return False
      elif(hex_dig1 not in lis):return None
    

