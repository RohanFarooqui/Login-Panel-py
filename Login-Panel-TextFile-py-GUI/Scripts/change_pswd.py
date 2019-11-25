import os
import hashlib
import getpass


def check_names_pswd(Name,Pswd):
  file = open("login.txt","r")
  for i in file:
   lis=[]
   k=(i.split(' '))
   lis.append(k[0])
   lis.append(k[1])
   lis[-1] = lis[-1].strip()
   file = open("login.txt","r")
   for i in file:
       k=(i.split(' '))
       lis.append(k[0])
       lis.append(k[1])
       lis[-1] = lis[-1].strip()
   for i in range(0,len(lis)):
      if(lis[i] == Name):
         if(lis[i+1] == Pswd):
           return True
         
def change_pswd(Name,Current_Pswd,New_Pswd,Cnfrm_new_Pswd):
   Name1= Name.upper()
   hash1= hashlib.md5(Name1.encode())
   hex_dig1 = hash1.hexdigest()
   Pswd = Current_Pswd
   hash2= hashlib.md5(Pswd.encode())
   hex_dig2 = hash2.hexdigest()
   if(check_names_pswd(hex_dig1,hex_dig2)== True):
      Pswd1= New_Pswd
      hash3=hashlib.md5(Pswd1.encode())
      hex_dig3 = hash3.hexdigest()
      Pswd2= Cnfrm_new_Pswd
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
      else:
         return None
   else:
      return False
   return True



