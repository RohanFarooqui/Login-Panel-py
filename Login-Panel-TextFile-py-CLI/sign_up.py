from check_name import check_names
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
