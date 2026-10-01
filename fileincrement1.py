#!/usr/bin/python

import os
import subprocess

singleinitvalue=1
singlefinalvalue=986114

tripleinitvalue=1
triplemidvalue1=991
triplemidvalue2=6
triplefinalvalue=986114

quadraplemidvalue=999


filepath="/opt/product/YOGESH/MIGFILES_SRG_LOAD"


multiinfofile=filepath+"/"+"HLR_SUBS_MULTI_CALL_INFO.csv"
hlrnmsinfofile=filepath+"/"+"HLR_NMS_SUBS_ALLOC_INFO.csv"
hlrsubsempfile=filepath+"/"+"HLR_SUBS_EMLPP_INFO.csv"

hlrsubsssinfo=filepath+"/"+"HLR_SUBS_CUG_FEATURE_LIST.csv"
hlrsubscwinfo=filepath+"/"+"HLR_SUBS_CUG_INFO.csv"
hlrsubscuginfo=filepath+"/"+"HLR_SUBS_CW_INFO.csv"
hlrsubscugfeaturelist=filepath+"/"+"HLR_SUBS_SS_INFO.csv"

hlrsubscbinfo=filepath+"/"+"HLR_SUBS_CB_INFO.csv"
hlrsubscfwdinfo=filepath+"/"+"HLR_SUBS_CFWD_INFO.csv"
hlrsubslineinfo=filepath+"/"+"HLR_SUBS_LINE_IDENT_INFO.csv"



input=input("Please enter the file to be generated 1. multiinfofile 2. hlrnmsinfofile 3. hlrsubsempfile 4.ALL 5.hlrsubsssinfo 6.hlrsubscwinfo 7.hlrsubscuginfo 8.hlrsubscugfeaturelist 9.hlrsubscbinfo 10.hlrsubscfwdinfo 11.hlrsubslineinfo\n")
print(input)

def singlevaluefunc(input):

    if int(input) ==1:
        if os.path.exists(multiinfofile):
            os.remove(multiinfofile)
            print("File deleted successfully")
        generatefile(input,multiinfofile)

    elif int(input) ==2:
        if os.path.exists(hlrnmsinfofile):
            rc=os.remove(hlrnmsinfofile)
            print("File deleted successfully")
        generatefile(input,hlrnmsinfofile)


    elif int(input) ==3:
        if os.path.exists(hlrsubsempfile):
            rc=os.remove(hlrsubsempfile)
            print("File deleted successfully")
        generatefile(input,hlrsubsempfile)


    elif input ==4:

        if os.path.exists(multiinfofile):
            os.remove(multiinfofile)
        if os.path.exists(hlrnmsinfofile):
            os.remove(hlrnmsinfofile)
        if os.path.exists(hlrsubsempfile):
            os.remove(hlrsubsempfile)

        filelist =[multiinfofile,hlrnmsinfofile,hlrsubsempfile]

        generatefile(input,filelist)

        print("File deleted successfully")

    elif int(input) ==5:
        if os.path.exists(hlrsubsssinfo):
            rc=os.remove(hlrsubsssinfo)
            print("File deleted successfully")
        multigeneratefile(input,hlrsubsssinfo)


    elif int(input) ==6:
        if os.path.exists(hlrsubscwinfo):
            rc=os.remove(hlrsubscwinfo)
            print("File deleted successfully")
        multigeneratefile(input,hlrsubscwinfo)

    elif int(input) ==7:
        if os.path.exists(hlrsubscuginfo):
            rc=os.remove(hlrsubscuginfo)
            print("File deleted successfully")
        multigeneratefile(input,hlrsubscuginfo)

    elif int(input) ==8:
        if os.path.exists(hlrsubscugfeaturelist):
            rc=os.remove(hlrsubscugfeaturelist)
            print("File deleted successfully")
        multigeneratefile(input,hlrsubscugfeaturelist)

    elif int(input) ==9:
        if os.path.exists(hlrsubscbinfo):
            rc=os.remove(hlrsubscbinfo)
            print("File deleted successfully")
        multigeneratefile(input,hlrsubscbinfo)


    elif int(input) ==10:
        if os.path.exists(hlrsubscfwdinfo):
            rc=os.remove(hlrsubscfwdinfo)
            print("File deleted successfully")
        multigeneratefile(input,hlrsubscfwdinfo)


    elif int(input) ==11:
        if os.path.exists(hlrsubslineinfo):
            rc=os.remove(hlrsubslineinfo)
            print("File deleted successfully")
        multigeneratefile(input,hlrsubslineinfo)


def generatefile(input,*args):
    print(args)
    if len(args)>1:
        for fileiterate in args[0]:
            for i in range(singleinitvalue,singlefinalvalue+1):
                filewrite=open(fileiterate,"a+")
                filewrite.write(str(i))
                filewrite.write("\n")
                if i==singlefinalvalue:
                    print("File writing completed for file %s upto %s" %(fileiterate,singlefinalvalue))
                    break

    else:
        for i in range(singleinitvalue,singlefinalvalue+1):
            filewrite=open(args[0],"a+")
            filewrite.write(str(i))
            filewrite.write("\n")
            if i==singlefinalvalue:
                print("File writing completed for file %s upto %s" %(args[0],singlefinalvalue))
                break

def multigeneratefile(input,*args):
    count=0
    datacountlist=getcount(triplefinalvalue)
    for i in range(tripleinitvalue,triplefinalvalue+1):
        triplemidvalue1=991
        incrementvalue=1
        for j in range(triplemidvalue2):
            filewrite=open(args[0],"a+")
            if int(input) in [9,10,11]:
                filewrite.write(str(i)+","+str(quadraplemidvalue)+","+str(triplemidvalue1)+","+str(incrementvalue))
            else:
                filewrite.write(str(i)+","+str(triplemidvalue1)+","+str(incrementvalue))
            filewrite.write("\n")
            triplemidvalue1=triplemidvalue1+1
            incrementvalue=incrementvalue+1
        count=count+1
        if count in datacountlist:
            print("File has completed upto %s" %count)
    print("File writing completed for file %s upto %s" %(args[0],triplefinalvalue))

def getcount(triplefinalvalue):
    datacountlist=[]
    print("value is %s" %(triplefinalvalue//30))
    stepvalue=triplefinalvalue//30
    for i in range(stepvalue,triplefinalvalue,stepvalue): 
        datacountlist.append(i)
    return datacountlist

singlevaluefunc(input)

