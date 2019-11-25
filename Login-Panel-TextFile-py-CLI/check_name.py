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
