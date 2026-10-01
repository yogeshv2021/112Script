import os    
import time
import threading
import time
import csv
import pandas as pd
import json
import os
import logging
import datetime
import sqlite3
import requests


#getrows = getdbresult()
reportpath = "/opt/product/YOGESH/reportpath"
current_file_time= time.time()
current_time=datetime.datetime.fromtimestamp(current_file_time).strftime('%Y-%m-%d %H:%M:%S')
filename = "ChatBot_Report_" + current_time + ".csv"
reportfilename = reportpath + filename
print(reportfilename)

rows=[
("a","b","c"),
("d","e","f")
]

with open(reportfilename,"w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
        

