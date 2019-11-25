import os
import hashlib
import getpass
#from side_function import timer
#from side_function import remove_space

def Login_check(Name,Pswd):
 n = 3
 Name1= Name.upper()
 hash1= hashlib.md5(Name1.encode())
 hex_dig1 = hash1.hexdigest()
 #while(n > 0):
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
       '''n=n-1
       if(n > 0):print(n," Tries Left, Total Tries are '3' ")         
       if(n==0):
         print("Max tries Limit i.e 3 reached, Try Again")'''
       return False
  elif(hex_dig1 not in lis):return None
    

'''

x=Login_check("Rohan","1234")

if(x == True):
     print("Welcome")
elif(x == False):
     print("Password is Incorrect, but user in data base")
     
elif(x == None):
     print("User Not in Database")'''

