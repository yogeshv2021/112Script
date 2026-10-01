#/usr/bin/python

import sys
import os

try:
    File_name = sys.argv[1:][0]
    print(File_name)
    File_split = File_name.split(".")[0]
    File_ext = File_name.split(".")[-1]
    if os.path.exists("/opt/product/YOGESH/" + File_name):
        print("File is present")
    else:
        print("File is not present")
        quit() 

except (NameError,IndexError):
    print("Please enter proper file name with extension")
    quit()

with open(File_name,"r+") as fileread:
    a = fileread.readlines()
    c = len(a)
    increment = 1
    filecount = 1
    while increment <= 10000:
        for i in a:
           with open(File_split +str(filecount) + File_ext,"a+") as filewrite:
               filewrite.write(str(i))
               if increment == 10000:
                   print(int(increment*filecount))
                   if int(increment*filecount) == c:
                       sys.exit()
                   else:
                       increment = 1
                       filecount = filecount +1

               else:
                   increment = increment +1
                   print(increment)
