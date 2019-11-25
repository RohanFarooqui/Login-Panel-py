def check_names(Name):
  file = open("login.txt", "r")
  lis=[]
  for i in file:
   k=(i.split(' '))
   lis.append(k[0].upper())
   #lis[-1] = lis[-1].strip()
  length = len(lis)
  if(Name.upper() in lis):
     file.close
     return  True
  else:
     file.close
     return False


def sign_up(Name,Pswd):
  if(check_names(Name) == True):
    return False
  elif(check_names(Name) == False):
   with  open("login.txt","a") as filew:
    filew.write(Name)
    filew.write(" ")
    filew.write(Pswd+'\n')
    filew.close
    return True
  else:
    return False


