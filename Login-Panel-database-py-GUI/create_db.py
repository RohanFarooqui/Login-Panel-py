##Import
import pymysql
import os
#Declare Variables
db_name   = "login"
##db variable
Db_link   = "localhost"
username  = "root"
pswd      = ""


##Check Database
def check_database():
 global  db_name
 global  Db_link
 global  username
 global  pswd
 mydb = pymysql.connect(Db_link,username,pswd)
 mycursor = mydb.cursor()
 mycursor.execute("SHOW DATABASES")
 for x in mycursor:
    if(x[0] == db_name):
         return True

##Check Table 
def check_table():
   global  Db_link
   global  username
   global  pswd
   global  db_name
   db = pymysql.connect(Db_link,username,pswd,db_name)
   cursor = db.cursor()
   sql    = ("""SELECT Name from login.login_app  """)
   try:
      cursor.execute(sql)                                                                                                                                                            
      db.close()                                                                                           
      return True
   except:
      db.rollback()                                                                                        
      db.close()                                                                                           
      return False


##Create db    
def create_db():
 global  db_name
 global  Db_link
 global  username
 global  pswd
 mydb = pymysql.connect(Db_link,username,pswd)
 mycursor = mydb.cursor()
 mycursor.execute("CREATE DATABASE login")



##Create Table
def create_table():
 global  db_name
 global  Db_link
 global  username
 global  pswd
 mydb = pymysql.connect(Db_link,username,pswd,db_name)
 mycursor = mydb.cursor()
 mycursor.execute("""CREATE TABLE IF NOT EXISTS login_app (
                     Name  VARCHAR(500),Password  VARCHAR(200))""")
 mydb.commit()
              
 
###main###
if(check_database()== True):
    print("Database Exist")
    if(check_table()   == True): print("Table Exist")
    else:
        create_table()
        print("Table is Created Sucessfully ...!")
else:
    print("Db and table not Exist we are creating...")
    create_db()
    create_table()
    print("Table and Database is Created Sucessfully..!")

os.system("PAUSE")
