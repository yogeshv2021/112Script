#!/usr/bin/python

import string
import random
import os

filepath="/opt/product/YOGESH/"
filename="ITGfile_4.txt"
Total_number_of_values=20000
completepath=filepath + filename


def id_generator(firstsize=3,secondsize=6, chars=string.ascii_uppercase):
    if os.path.exists(completepath):
        filedelete=open(completepath,"w")
        filedelete.close()
    else:
        pass
    checklist=[]
    for i in range(Total_number_of_values):
        data1=''.join(random.choice(chars) for _ in range(firstsize))
        data2=''.join(random.choice(chars) for _ in range(secondsize))
        combinedata=data1 + "-" + data2
        if combinedata not in checklist: 
            checklist.append(combinedata)
            print(combinedata)
            filewrite(combinedata)

def filewrite(combinedata):
     with open(completepath,"a+") as filecreate:
         filecreate.write(combinedata + "\n")
id_generator()

