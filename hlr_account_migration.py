import os
import subprocess
import paramiko
import re
import cx_Oracle

user="autoadmin"
hostname="192.168.151.90"
key="/root/.ssh/id_rsa.pub"

dir1 = '/opt/product/AUTOMATION/AUTOMATION_RESULTS/LINUX/HLR/RESULTS/HLR_5.0.0.0/Rev2/2019_01_24_11_34_45/AUTO_HLR_MM'
dir2 = '/opt/product/AUTOMATION/TEST_AUTOMATION_FRAMEWORK/HLR_BKP/INPUTS/INPUT_PATH'
dictaccmap = {}

getdircmd='ls -d '+ dir2 + '/*'
getfilecmd='egrep -r "account_id|ACCOUNT_ID" '
greppattern="(account_id[(\s)*(<|>)*=(\s)*[']*[0-9]+|ACCOUNT_ID[(\s)*=(\s)*[']*[0-9]+)"
chkactdatequery="select account_id,first_activation_date from hlr_account where account_id="
fetchaccquery="select account_id from hlr_account where account_id="
username  = 'HLR_AUTO'
password  = 'LYCA'
ip_address  = '192.168.151.166'
service_name = 'STNEWDB'


class Connect():

    def __init__(self,hostname,user,key):

        self.hostname=hostname
        self.user=user
        self.key=key

    def connectclientserver(self):
        self.sshclient = paramiko.SSHClient()
        self.sshclient.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        print(self.hostname,self.user,self.key)
        try:
            self.sshclient.connect(self.hostname,username=self.user,key_filename=self.key)
            server._checkfile()
            server.getdirectcommand()
        except Exception as connectionfail:
            print("Failure occured %s" %connectionfail)

    def getdirectcommand(self):
        try:
            (stdin,stdout,stderr)=self.sshclient.exec_command(getdircmd)
            for readfd in stdout:
                folderlist=readfd
                server.getaccuntidfiles(folderlist)
        except Exception as stderr:
            print("Failure occured while fetching directories %s" %stderr)

    def getaccuntidfiles(self,flist):
        try:
            (stdin,stdout,stderr)=self.sshclient.exec_command(getfilecmd +" " + flist)
            for readfl in stdout:
                filelist=readfl
                filename=filelist.split(":")[0]
                query=filelist.split(":")[-1]
                server.fileaccntidmapp(filename,query)
        except Exception as stderr:
            print("Failure occured while fetching directories %s" %stderr)

    def fileaccntidmapp(self,filename,query):
        try:
            getacciterlst = re.findall(greppattern, query)
            for getaccitergp in getacciterlst:
                getaccitersp = getaccitergp.split("=")[1]
                if getaccitersp:
                    getacctiterst = getaccitersp.strip("'")
                    getacct = getacctiterst.replace("'","")
                    getacct = getacct.strip(" ")
                    server.checkaccountstatus(filename,query,getacct)
                
        except Exception as stderr:
            print("Failure occured while fetching directories %s,%s" %(query,stderr))

    def checkaccountstatus(self,filename,query,getacct):
        try:
            connection_string=username+"/"+password+"@"+service_name
            con=cx_Oracle.connect(connection_string)
            cur=con.cursor()

            if cur:
                querystring=chkactdatequery + "'" + getacct + "'"
                cur.execute(querystring)
                resp=cur.fetchone()
                acctlist=list(resp)
                getaccvalue=",".join(map(str,acctlist))
                currentpath=os.getcwd()
                os.chdir(currentpath)
                with open("getactdate.txt","a+") as filewrite:
                    filewrite.write(getaccvalue+"\n")
                os.system("chmod +x getactdate.txt;chown testteam:testteam getactdate.txt")
                server.getnewaccdb(filename,query,getacct)

        except Exception as stderr:
            print("Failure occured while fetching activationdate %s,%s" %(query,stderr))


    def _checkfile(self):
        try:
            currentpath=os.getcwd()
            os.chdir(currentpath)
            print(os.path.exists("getactdate.txt"))
            if os.path.isfile("getactdate.txt"):
                os.system("rm -rf getactdate.txt")
                print("Existing File deleted successfully.Creating new file.")
            else:
                print("File not found to delete.Hence creating the file with header")

            with open("getactdate.txt","a+") as filewrite:
                filewrite.writelines(['Account_id,','First_Activation_date'])
                filewrite.write("\n")

        except Exception as fileerror:
            print("Exception occured while deleting files %s" %fileerror) 


    def getnewaccdb(self,filename,query,getacct):
        try:
           connection_string=username+"/"+password+"@"+service_name
           con=cx_Oracle.connect(connection_string)
           cur=con.cursor()
          
           if cur:
               querystring=fetchaccquery + "'" + getacct + "'"
               cur.execute(querystring)
               resp=cur.fetchone()
               print(resp)
               #server.updatefile(filename,getacct,resp)
        
        except Exception as dberror:
            print("Failure occured during db execution %s" %dberror)

    def updatefile(self,filename,oldacctid,newacctid):
        try:

            print(filename,oldacctid,newacctid)
            replacecmd="sed -i " + "'s/\<" + oldacctid + "\>/" + newacctid[0] + "/g;'" + " " + filename
            (stdin,stdout,stderr)=self.sshclient.exec_command(replacecmd)
            print(stdout)

    #        sftpconn= self.sshclient.open_sftp()
    #        getfilecontent = sftpconn.open(filename,'r+')
    #        getcontent = getfilecontent.read().decode()
    #        getreplcontent = re.sub(oldacctid,newacctid[0],getcontent)
    #       print(getreplcontent)
    #        getwritecontent = sftpconn.open(filename,'w+')
    #        getwritecontent.write(getreplcontent)

        except Exception as fileupdateerror:
            print("Failure occured during file updation %s" %fileupdateerror)

    def disconnectserver(self):
        self.sshclient.close()

if __name__== "__main__":
    server = Connect(hostname,user,key)
    server.connectclientserver()
