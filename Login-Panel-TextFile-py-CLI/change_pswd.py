##Import Goes Here ###
##Import Libraries 
import os
import hashlib
import getpass
import time
##Import Files
from check_name_pswd import check_names_pswd


def change_pswd():
   os.system('cls')
   Name = str(input("                            Enter Your Name : "))
   Name1= Name.upper()
   hash1= hashlib.md5(Name1.encode())
   hex_dig1 = hash1.hexdigest()

   Pswd = getpass.getpass("                            Enter your Current password: ")
   hash2= hashlib.md5(Pswd.encode())
   hex_dig2 = hash2.hexdigest()
      
   if(check_names_pswd(hex_dig1,hex_dig2)== True):
      Pswd1= getpass.getpass("                            Enter your New password :")
      hash3=hashlib.md5(Pswd1.encode())
      hex_dig3 = hash3.hexdigest()

      Pswd2= getpass.getpass("                            Re-Enter your password :")
      hash4=hashlib.md5(Pswd2.encode())
      hex_dig4 = hash4.hexdigest()
      if(hex_dig3 == hex_dig4):
         with open("login.txt","r") as file:
            m=[]
            for i in file:
               l=()
               k=(i.split(' '))
               k[-1] = k[-1].strip()
               l=l+tuple (k)
               m.append(l) 
         for i in range(0,len(m)):
            if(m[i][0] ==hex_dig1):
             if(m[i][1] == hex_dig2):
                  k=list(m[i])
                  k[1]=hex_dig4
                  m.append(tuple (k))
            else:
               continue
         m.remove((hex_dig1, hex_dig2))
         with open("login.txt","r+") as file1:
          for i in m:
            file1.write(i[0])
            file1.write(" ")
            file1.write(i[1]+'\n')
         file.close()
         return True
      else:
         print("                            Password NOT match")
         time.sleep(1)
   else:
      print("                            Current Password is INCORRECT")
      time.sleep(1)
