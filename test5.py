#!/usr/bin/python
import json
comparedata ={}
finaldata ={}
increment = 1

comparatorfile = "/opt/product/AUTOMATION_REPORT/flaskr/Report/config/Comparatorfile.json"
comparatorfiledst = "/opt/product/AUTOMATION_REPORT/flaskr/Report/config/Comparatorfile_bkp.json"
with open(comparatorfile,mode="rb") as fileread:
    print(fileread)
    comparedata ={}
    finaldata ={}
    increment = 1
    compread = fileread.read().decode(errors='ignore')
    dictcompread = json.loads(compread)
    for key,items in dictcompread.items():
        for key1,items1 in items.items():
            for key2 in items1:
                k=key2['Format_Type'].keys()
                for i in k:
                    print(key2['Format_Type'][i])
                tdrvalue = key2['Format_Type']
#                print(key2["Report_Crossteam"],key2['Report_Products'],tdrvalue)
                for tdrkey,tdrvalue in tdrvalue.items():
                    comparedata["data" + str(increment)] = {"Report_Crossteam" : key2['Report_Crossteam'],"Report_Products" : key2['Report_Products'],"Report_TDR" : tdrkey,"Report_header": tdrvalue[0],"Report_separator": tdrvalue[1]}
#                    comparefinaldata = json.dumps(comparedata,indent=4)
                    increment = increment + 1
#                    print(comparefinaldata)

with open(comparatorfiledst,mode="w+") as filewrite:
    compread = json.dump(comparedata,filewrite,indent=4)
#    print(compread)

