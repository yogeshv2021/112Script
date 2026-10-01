#/usr/bin/python

import sys

first_input = sys.argv[1]
print(len(first_input))
sys.exit()

with open("file.txt","r+") as fileread:
    a = fileread.readlines()
    c = len(a)
    increment = 1
    filecount = 1
    while increment <= 10000:
        for i in a:
           with open("file" +str(filecount) + ".txt","a+") as filewrite:
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
