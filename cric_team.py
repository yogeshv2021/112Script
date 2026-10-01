#!/usr/bin/python

import random
import math
import copy
import time
import pandas as pd
import csv

numberofteams=1

MI=['IshanKishan','RohitSharma','CameroonGreen','SurykumarYadav','TilakVerma','TimDavid','PChawla','ChrisJordan','Shokeen','Behrondoff','AMadhwal','Wedhereve']
GT=['WSaha','ShubhnamGill','HardikPandya','VijayShankar','DavidMiller','RahulTewatiya','Shanka','RashidKhan','Nalkande','Mohitsharma','NoorAhmed','Mshami']
ListCaption=['Captain','ViceCaptain','Player2','Player3','Player4','Player5','Player6','Player7','Player8','Player9','Player10','Player11']

#Team=['DConvey','MDhoni','RGaikwad','SDube','ARahane','ARayadu','RJadeja','MAli','DChahar','TDeshpande','MPathirana','MThekshana','WSaha','ShubhnamGill','HardikPandya','DavidMiller','RahulTewatiya','RashidKhan','Jlittle','Mohitsharma','NoorAhmed','Mshami','SaiSudharshan','VShankar']


#Team=["ArunPandiyan","Dinesh","Eswar","Jiiva","Klindan","Lilith","Lokishore","MohanBabu","MohanPandiyan","Naresh D","Naresh","Naveen","Nikhil","Nitin","Pranav","Prashanth","Rajesh","Sadiq","SaiVignesh","Sakthivel","Sandeep","Suresh","Vamsi","Vasu","Vignesh","Vijendran","Yogendra","Yogesh","Yuvaraj","marishwaran","nikilesh","sanjay","rajeshkanna","mohamad kaif","vishnu","balasurya"]
Team=["Rajesh","Mohan Pandian","Mohan Babu","Sakthivel","Yogesh","Dinesh","Lilith","Sanjay","Suresh","Vasu","Vamsi","Sai Vignesh","Nithin","Sandeep","Klindan","Sadhiq","Sathyaraj","Sashank","Vishnu","Mariswaran","Naveen"]

#dictTeam={'WSaha':45,'DConvey':88,'ShubhnamGill':93,'MDhoni':10,'RGaikwad':92,'SDube':58,'ARahane':24,'SaiSudharshan':44,'ARayadu':3,'HardikPandya':75,'MAli':21,'RJadeja':94,'DChahar':66,'TDeshpande':28,'MPathirana':56,'MThekshana':18,'RahulTewatiya':2,'RashidKhan':88,'Mohitsharma':61,'Mshami':79,'DavidMiller':20,'NoorAhmed':14,'VShankar':12,'Jlittle':6}
#WicketKeeper=['DConvey','WSaha']
#Batsman=['MDhoni','RGaikwad','SDube','ARahane','ARayadu','ShubhnamGill','SaiSudharshan','DavidMiller','VShankar']
#AllRounder=['HardikPandya','RJadeja','MAli']
#Bowler=['DChahar','TDeshpande','MThekshana','MPathirana','RahulTewatiya','RashidKhan','Jlittle','Mohitsharma','Mshami','NoorAhmed']

#Team=["ArunPandiyan","Dinesh","Eswar","Jayasuriya","Jiiva","Klindan","Lilith","Lokishore","MohanBabu","MohanPandiyan","Monish","Nannu","Naresh D","Naresh","Naveen","Nikhil","Nitin","PrabhuDoss","Prakash","Pranav","Prashanth","PriyaRajan","Rajesh","Sadiq","SaiVignesh","Sakthivel","Sandeep","Selvendran","Suresh","Vamsi","Vasu","Vignesh","Vijendran","Yogendra","Yogesh","Yuvaraj"]

capvcdict={}
IndvTeam=[]
TotalTeamList=[]
players=7
counter=0
count=4

CntWicketKeeper=2
CntBatsman=4
CntAllRounder=2
CntBowler=3
checkplayercnt=[0,0,0,0]
innercount=[0,0,0,0]

captcounter=[65,30,0]
captselection=[70,20,10]
captincrementcounter=[0,0,0]

vicecaptcounter=[70,30,0]
vicecaptselection=[60,30,10]
viceincrementcounter=[0,0,0]



numberofteams=int(input("Please enter the number of Teams to generate: "))
#CntWicketKeeper=int(input("Please enter the number of Wicketkeepers to generate: "))
#CntBatsman=int(input("Please enter the number of Batsman to generate: "))
#CntAllRounder=int(input("Please enter the number of AllRounder to generate: "))
#CntBowler=int(input("Please enter the number of Bowler to generate: "))
TextFile=input("Please enter the File name to generate: ")

generatefilename="/opt/product/YOGESH/Cric/Team1/"+ TextFile +".csv"
    
#if (CntWicketKeeper + CntBatsman + CntAllRounder + CntBowler != players):
#    print("Summation of input values entered in not 11.Please check the input entered")
#    exit()


def getInputs():
    random.shuffle(Team)
    print(Team)
    with open(generatefilename,"w+") as file:
        wr=csv.writer(file)
        wr.writerow(ListCaption)
        wr.writerows(Team)
    return Team


def getInput():
#    for dictincrement in range(0,numberofteams+1)
    team1=random.shuffle(Team)
#    getlist=checkduplicate(getcapvc)
    print(team1)
    return team1

def randomgen_captain_vice(dictincrement,Team):
    print("Entered function for generating random players")
    random.shuffle(Team)

#    capvcdict[dictincrement]=[Team[0],Team[1]]
#    captainpercent=dictTeam[Team[0]]
#    vicecaptainpercent=dictTeam[Team[1]]
#    getvalue=randomgen_players(dictincrement,Team[0],Team[1],captainpercent,vicecaptainpercent)
#    print("If Limit reached %s" %getvalue)
#    if getvalue==0:
#        randomgen_captain_vice(dictincrement,Team)
#    print("captain counter %s" %captincrementcounter)
#    print("vicecaptain counter %s" %viceincrementcounter)
#    return capvcdict

def checkduplicate(getcapvc):
    newlist=list(getcapvc.values())
    getlist=list(set(tuple(sorted(iterlist)) for iterlist in newlist))
    return getlist

def randomgen_players(dictincrement,captain,vicecaptain,captainpercent,vicecaptainpercent):
    IndvTeam=[]
    IndvTeam.append(captain)
    IndvTeam.append(vicecaptain)
    newlist=[captain,vicecaptain]
    print("captain and vicecaptain %s" %(newlist))
    listcount=len(TotalTeamList)
    print("User Entered values are %s,%s,%s,%s" %(CntWicketKeeper,CntBatsman,CntAllRounder,CntBowler))
    Calculate_capvc_percent(newlist,listcount,dictincrement,captainpercent,vicecaptainpercent)
    time.sleep(1)

    TmpWicketKeeper=copy.deepcopy(WicketKeeper)
    TmpBatsman=copy.deepcopy(Batsman)
    TmpBowler=copy.deepcopy(Bowler)
    TmpAllRounder=copy.deepcopy(AllRounder)



    checkplayercnt=[0,0,0,0]
    innercount=[0,0,0,0]

    if captain in TmpWicketKeeper:
        innercount[0]+=1
    elif captain in TmpBatsman:
        innercount[1]+=1
    elif captain in TmpAllRounder:
        innercount[2]+=1
    elif captain in TmpBowler:
        innercount[3]+=1

    if vicecaptain in TmpWicketKeeper:
        innercount[0]+=1
    elif vicecaptain in TmpBatsman:
        innercount[1]+=1
    elif vicecaptain in TmpAllRounder:
        innercount[2]+=1
    elif vicecaptain in TmpBowler:
        innercount[3]+=1

    if innercount[0] >CntWicketKeeper or innercount[1] >CntBatsman or innercount[2] >CntAllRounder or innercount[3] >CntBowler:
        print("cap and vc count is more than user entered so regenerating the cap and vc")
        return 0
    

    if captain in TmpWicketKeeper:
        TmpWicketKeeper.remove(captain)
        checkplayercnt[0]+=1
    if vicecaptain in TmpWicketKeeper:
        TmpWicketKeeper.remove(vicecaptain)
        checkplayercnt[0]+=1
    if TmpWicketKeeper!=[]:
        random.shuffle(TmpWicketKeeper)
        for wk in TmpWicketKeeper:
            if checkplayercnt[0]==CntWicketKeeper:
                break
            else:
                IndvTeam.append(wk)
                checkplayercnt[0]+=1

    if captain in TmpBatsman:
        TmpBatsman.remove(captain)
        checkplayercnt[1]+=1
    if vicecaptain in TmpBatsman:
        TmpBatsman.remove(vicecaptain)
        checkplayercnt[1]+=1
    if TmpBatsman!=[]:
        random.shuffle(TmpBatsman)
        for bt in TmpBatsman:
            if checkplayercnt[1]==CntBatsman:
                break
            else:
                IndvTeam.append(bt)
                checkplayercnt[1]+=1

    if captain in TmpAllRounder:
        TmpAllRounder.remove(captain)
        checkplayercnt[2]+=1
    if vicecaptain in TmpAllRounder:
        TmpAllRounder.remove(vicecaptain)
        checkplayercnt[2]+=1
    if TmpAllRounder!=[]:
        random.shuffle(TmpAllRounder)
        for al in TmpAllRounder:
            if checkplayercnt[2]==CntAllRounder:
                break
            else:
                IndvTeam.append(al)
                checkplayercnt[2]+=1

    if captain in TmpBowler:
        TmpBowler.remove(captain)
        checkplayercnt[3]+=1
    if vicecaptain in TmpBowler:
        TmpBowler.remove(vicecaptain)
        checkplayercnt[3]+=1
    if TmpBowler!=[]:
        random.shuffle(TmpBowler)
        for bo in TmpBowler:
            if checkplayercnt[3]==CntBowler:
                break
            else:
                IndvTeam.append(bo)
                checkplayercnt[3]+=1

    if (len(TotalTeamList))==dictincrement+1:
        pass
    else:
        TotalTeamList.append(IndvTeam)
    print("Team is %s,%s" %(TotalTeamList,dictincrement))

def Calculate_capvc_percent(newlist,listcount,dictincrement,captainpercent,vicecaptainpercent):
    getcaptainpercent=0
    getvicecaptainpercent=0
    capct=0
    vcapct=0
    print(captcounter,captainpercent)

    if (listcount > numberofteams or (viceincrementcounter[0] + viceincrementcounter[1] + viceincrementcounter[2] ==numberofteams and captincrementcounter[0] + captincrementcounter[1] + captincrementcounter[2] ==numberofteams)):
        print("Max number of Teams limit reached.so exiting...") 
        print("Final list Before inserting into CSV file... %s" %TotalTeamList)
        with open(generatefilename,"w+") as file:
            wr=csv.writer(file)
            wr.writerow(ListCaption)
            wr.writerows(TotalTeamList)
            exit()


    for i,j in enumerate(captcounter):
        if captainpercent>=j:
            captincrementcounter[i]+=1
            print("increment before %s" %captincrementcounter[i])
            break
    for k,l in enumerate(vicecaptcounter):
        if vicecaptainpercent>=l:
            viceincrementcounter[k]+=1
            break

    print("captain data %s" %captincrementcounter)
    print("vicecaptain data %s" %viceincrementcounter)
    print(i,captincrementcounter,getcaptainpercent)

    getvicecaptainpercent=round((numberofteams/100) * vicecaptselection[k])
    getcaptainpercent=round((numberofteams/100) * captselection[i])
    if (captincrementcounter[i]>getcaptainpercent or viceincrementcounter[k]>getvicecaptainpercent):
        captincrementcounter[i]-=1
        viceincrementcounter[k]-=1
        print("Entered function for generating player since captain percent count is reached")
        randomgen_captain_vice(dictincrement,Team)

getInputs()
#randomgen_captain_vice(dictincrement,Team)
