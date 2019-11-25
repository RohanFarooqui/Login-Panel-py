##Imports
import pymysql
##File Imports
try:
 from Scripts.side_function import *
except:
 from side_function import *

####DATABASE LINKING

##Side Function

##Check Db Connection
def db_connection():
   Db_link       = "localhost"
   username      = "root"
   pswd          = ""
   database_name = "login"
   try:
       db = pymysql.connect(Db_link,username,pswd,database_name)                                                #Connection with Database
       return True
   except Exception as e:
       return e

 
#Search User
def search_user_by_name(name):
   Db_link       = "localhost"
   username      = "root"
   pswd          = ""
   database_name = "login"
   hash1_name=hashing(name)  
   db = pymysql.connect(Db_link,username,pswd,database_name)                                                #Connection with Database
   cursor =  db.cursor()
   sql    = ("""SELECT Name,Password from login_app WHERE  Name = (%s) """)                                 #Query
   data   = hash1_name,                                                                                     #Data from GUI
   try:
      cursor.execute(sql,data)                                                                              #Query Execute
      result = cursor.fetchall()                                                                            #Fetch Data
      pswd= (result[0])                                                                                     #Get Password from Tuple
      db.close()                                                                                            #disconnect from server
      return True
   except:
      db.rollback()                                                                                         #Rollback in case there is any error
      db.close()                                                                                            #disconnect from server
      return False

### Main Functions

##Add Users
def add_user(name,pwd):
   Db_link       = "localhost"
   username      = "root"
   pswd          = ""
   database_name = "login"
   hash1_name=hashing(name)                                                                                 #Convert to hash data  from gui
   hash2_pswd=hashing(pwd)  
   db = pymysql.connect(Db_link,username,pswd,database_name)                                                #Connection with Database
   cursor = db.cursor()                              
   sql=("""INSERT INTO login_app VALUES (%s, %s) """)                                                       #Query
   data = (hash1_name,hash2_pswd)                                                                           #Data from GUI
   try:
     x=cursor.execute(sql,data)                                                                             #Query Execute
     db.commit()                                                                                            #Commit your changes in the database
     db.close()                                                                                             #disconnect from server
     return True
   except:
     db.rollback()                                                                                          #Rollback in case there is any error
     db.close()                                                                                             #disconnect from server
     return False


##Login Function
def login_check(name,pwd):
   Db_link       = "localhost"
   username      = "root"
   pswd          = ""
   database_name = "login"
   hash1_name=hashing(name)                                                                                 #Convert to hash data  from gui
   hash2_pswd=hashing(pwd)                                                                                  #Convert to hash data  from gui
   if(search_user_by_name(name)== True):
      db = pymysql.connect(Db_link,username,pswd,database_name)                                             #Connection with Database
      cursor =  db.cursor()
      sql    = ("""SELECT Name,Password from login_app WHERE  Name = (%s) """)                              #Query
      data   = hash1_name,                                                                                  #Data From GUI
      cursor.execute(sql,data)                                                                              #Query Execute
      result = cursor.fetchall()                                                                            #Fetch Data
      psd= (result[0][1])                                                                                   #Get Password from Tuple
      if(psd != hash2_pswd):                                                                                #disconnect from server
         db.close()  
         return False
      else:
         db.close()                                                                                         #disconnect from server
         return True
   else: 
        return None

##Update Pswd Function
def update_pswd(name,current_pswd,new_pswd):
   Db_link       = "localhost"
   username      = "root"
   pswd          = ""
   database_name = "login"
   hash1_name    = hashing(name)                                                                            #Convert to hash data  from gui
   hash2_pswd    = hashing(current_pswd)                                                                    #Convert to hash data  from gui
   hash3_newpswd = hashing(new_pswd)                                                                        #Convert to hash data  from gui
   if((login_check(name,current_pswd) == True)):
      db = pymysql.connect(Db_link,username,pswd,database_name)                                             #Connection with Database
      cursor =  db.cursor()
      sql    = ("""UPDATE login_app SET Password = (%s)  WHERE  Name = (%s) """)                            #Query
      data   = (hash3_newpswd,hash1_name) 
      cursor.execute(sql,data)                                                                              #Query Execute                                                                                   #Get Password from Tuple
      db.commit()                                                                                           #Commit Changes in DB
      db.close()                                                                                            #disconnect from server
      return True
   elif((login_check(hash1_name,hash2_pswd) == False)):
      return False
   else:
      return None

    


