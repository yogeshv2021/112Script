#!/usr/bin/python


from xml.dom import minidom
import socket
import os
import time

server_ip="192.168.151.77"
server_port=4720
cc=61
sim_structure="F209010800100101"
tdr_id="20200505194952HLR5028000001:20200505194951028001"
msisdnfile="/opt/product/YOGESH/msisdn.txt"
outputfile="/opt/product/YOGESH/fileout.csv"

sleep_btw_requests=2
total_bytes=501

xmlrequest="<LOCALIMSIREQ><REQUESTTYPE>LocalIMSIReq</REQUESTTYPE><MSISDN>6811240093</MSISDN><CC>0</CC><REQTYPE>1</REQTYPE><CHANNELID>8</CHANNELID><REQCAT>1</REQCAT><SIM_STRUCTURE>F209010800100101</SIM_STRUCTURE><INITIATION_TYPE>D</INITIATION_TYPE><TDR_ID>20200505194952HLR5028000001:20200505194951028001</TDR_ID></LOCALIMSIREQ>"


def xml_frame():
    try:
        fileread = open(msisdnfile,"r+")
        getmsisdnlist = fileread.readlines()
        tree = minidom.parseString(xmlrequest)
        getmsisdnelement = tree.getElementsByTagName('MSISDN')
        getccelement = tree.getElementsByTagName('CC')
        for msisdn in getmsisdnlist:
            spacechkmsisdn= msisdn.strip()
            getmsisdnelement[0].firstChild.nodeValue=spacechkmsisdn
            getccelement[0].firstChild.nodeValue=cc
            newrequest = tree.toxml()
            spaceadd = total_bytes - len(newrequest)
            sendrequest = newrequest.ljust(len(newrequest)+ spaceadd)
            sendtoapp(spacechkmsisdn,sendrequest)
    except Exception as e:
        print("Error occured while framing %s" %e)


def sendtoapp(msisdn,sendrequest):
    try:
        tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcpsocket.connect((server_ip,server_port))
        print(sendrequest)
        req = tcpsocket.send(sendrequest)
        resp = tcpsocket.recv(6024)
        redirectoutput(msisdn,resp)
        tcpsocket.close()
    except Exception:
        print("Error occured while send or received")

def redirectoutput(msisdn,response):
    try:
       newresponse=response.replace('\x00','')
       print(newresponse)
       resptree = minidom.parseString(newresponse)
       returncode= resptree.getElementsByTagName('RETURNCODE')[0].firstChild.nodeValue
       returndescription= resptree.getElementsByTagName('RETURNDESC')[0].firstChild.nodeValue
       if os.path.isfile(outputfile) == False:
           writefile= open(outputfile,"w+")
           writefile.write("msisdn" + "," + "returncode" + "," + "returndescription"+ "\n")
           writefile.write(msisdn + "," + returncode + "," + returndescription+ "\n")
           writefile.close()
       else:
           writefile= open(outputfile,"a+")
           writefile.write(msisdn + "," + returncode + "," + returndescription+ "\n")
           writefile.close()
    except Exception:
        print("Error occured while writing the stats")

xml_frame()

