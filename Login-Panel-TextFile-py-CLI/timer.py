##Import Goes Here ###
##Import Libraries 
import os
import time

### Code start Here ###
def timer(n):
  while(n >= 0):
    time.sleep(1)
    os.system('cls')
    print("                            wait ",n," Second ")
    n=n-1
