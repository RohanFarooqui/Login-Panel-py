import os 

def check_names_pswd(Name,Pswd):
  file = open("login.txt","r")
  for i in file:
   lis=[]
   k=(i.split(' '))
   lis.append(k[0])
   lis.append(k[1])
   lis[-1] = lis[-1].strip()
   if((Name == lis[0]) and (Pswd != lis[1])):
    ndecider = True
    pdecider = False
    break
   elif((Name == lis[0]) and (Pswd == lis[1])): 
    ndecider = True
    pdecider = True
    break
   elif((Name != lis[0]) and (Pswd != lis[1])):
     del lis[0]
     del lis[0]
   else:
     ndecider = False
  if((ndecider == True) and (pdecider == True)):
     return True
  else:
     return False

