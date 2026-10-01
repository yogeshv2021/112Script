#!/usr/bin/python

import os
import socket
import time
import re

#remote_server_ip = "192.168.151.143"
#remote_server_port = 8122

outbound_server_ip = "192.168.151.143"
outbound_server_port = 3628

local_ip = "192.168.151.143"  # Standard loopback interface address (localhost)
local_port = 8196  # Port to listen on (non-privileged ports are > 1023)

length=9


xmlresponse1="<SPENDING_LIMIT_ANSWER><SESSIONID>pcrfdiastack.plint.pcrf.net;1669034897;563518;34:11</SESSIONID><ERROR_CODE>0</ERROR_CODE><ERROR_DESC>Success</ERROR_DESC><MSISDN>449697989914</MSISDN><NETWORKID>48</NETWORKID><REDIRECT_PROFILE_ID>101</REDIRECT_PROFILE_ID><REQ_TYPE>0</REQ_TYPE><POLICY_COUNTER_STATUS_REPORT><POLICY_COUNTER_INFO><COUNTER_IDENTIFIER>23</COUNTER_IDENTIFIER><COUNTER_STATUS>GLOBAL REGION1</COUNTER_STATUS><ENABLE_4G>1</ENABLE_4G></POLICY_COUNTER_INFO><PENDING_POLICY_COUNTER_INFO><COUNTER_STATUS>GLOBAL REGION1</COUNTER_STATUS><PENDING_POLICY_COUNTER_CHANGE_TIME>20221122000000</PENDING_POLICY_COUNTER_CHANGE_TIME></PENDING_POLICY_COUNTER_INFO><POLICY_COUNTER_INFO><COUNTER_IDENTIFIER>51</COUNTER_IDENTIFIER><COUNTER_STATUS>HOME_COUNTER</COUNTER_STATUS><ENABLE_4G>0</ENABLE_4G></POLICY_COUNTER_INFO><PENDING_POLICY_COUNTER_INFO><COUNTER_STATUS>HOME_COUNTER</COUNTER_STATUS><PENDING_POLICY_COUNTER_CHANGE_TIME>20221122000000</PENDING_POLICY_COUNTER_CHANGE_TIME></PENDING_POLICY_COUNTER_INFO></POLICY_COUNTER_STATUS_REPORT></SPENDING_LIMIT_ANSWER>"

xmlresponse2="<SESSION_TERMINATION_RESPONSE><MSISDN>449697989914</MSISDN><SESSIONID>pcrfdiastack.plint.pcrf.net;1669034626;177993;34:7</SESSIONID><ERROR_CODE>1</ERROR_CODE><ERROR_DESC>Service_Not_Allowed</ERROR_DESC></SESSION_TERMINATION_RESPONSE>"

xmlrequest3="<SPENDING_STATUS_NOTIFICATION_REQUEST><MSISDN>449697989914</MSISDN><SESSIONID>909683901231</SESSIONID><NETWORKID>48</NETWORKID><POLICY_COUNTER_STATUS_REPORT><POLICY_COUNTER_INFO><COUNTER_IDENTIFIER>4697</COUNTER_IDENTIFIER><COUNTER_STATUS>3G</COUNTER_STATUS></POLICY_COUNTER_INFO><PENDING_POLICY_COUNTER_INFO><COUNTER_STATUS>4G</COUNTER_STATUS><PENDING_POLICY_COUNTER_CHANGE_TIME>20221128000000</PENDING_POLICY_COUNTER_CHANGE_TIME></PENDING_POLICY_COUNTER_INFO><POLICY_COUNTER_INFO><COUNTER_IDENTIFIER>4698</COUNTER_IDENTIFIER><COUNTER_STATUS>4G_FUP</COUNTER_STATUS></POLICY_COUNTER_INFO><PENDING_POLICY_COUNTER_INFO><COUNTER_STATUS>4G_FUP</COUNTER_STATUS><PENDING_POLICY_COUNTER_CHANGE_TIME>20221203000000</PENDING_POLICY_COUNTER_CHANGE_TIME></PENDING_POLICY_COUNTER_INFO></POLICY_COUNTER_STATUS_REPORT></SPENDING_STATUS_NOTIFICATION_REQUEST>"

xmlresponse3="<SPENDING_STATUS_NOTIFICATION_ANSWER><SESSIONID>909683901231</SESSIONID><MSISDN>449697989914</MSISDN><RESULT_CODE>0</RESULT_CODE><ERROR_MESSAGE>Success</ERROR_MESSAGE></SPENDING_STATUS_NOTIFICATION_ANSWER>"

def xml_receive():

   try:
#       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       s.bind((local_ip, local_port))
       conn,address = s.accept()
       while True:
           count=0
           data = conn.recv(65535)
           print("Request received %s" %data)
           getregrequest=re.findall('PCRF_REGISTRATION',data)
           getstrrequest=re.findall('SESSION_TERMINATION_REQUEST',data)
           getslrrequest=re.findall('SPENDING_LIMIT_REQUEST',data)
           getsession=re.findall('<SESSIONID>.*</SESSIONID>',data)
           count+=1
           if getregrequest:
               print("Received registration request.Ignoring..")

           if getslrrequest:
               print("SLR request is received")
               getsession1=re.findall('<SESSIONID>.*</SESSIONID>',xmlresponse1)
               slrreq=xmlresponse1.replace(getsession1[0],getsession[0])
               lengthresp=len(slrreq)
               lengthrespdiff=length-len(str(lengthresp))
               fillregvalue=str(lengthresp).zfill(length)
               slresponse=fillregvalue+slrreq
               #xml_send()
               #time.sleep(5)
               conn.sendall(slresponse)
               #time.sleep(5)
               xml_send()


           if getstrrequest:
               getsession2=re.findall('<SESSIONID>.*</SESSIONID>',xmlresponse2)
               print("STR requets is received")
               strreq=xmlresponse2.replace(getsession2[0],getsession[0])
               lengthresp=len(strreq)
               lengthrespdiff=length-len(str(lengthresp))
               fillregvalue=str(lengthresp).zfill(length)
               stresponse=fillregvalue+strreq
               conn.sendall(stresponse)

   except Exception,error:
       print("Exception occured %s" %error)


def xml_send():

   try:
#        fileopen = open("/opt/product/testteam/Products/Saivignesh/testlim_bkp.data","r+")
#        r1 = fileopen.readlines()
#        for i in r1:
#            spaceadd = len(i)+384
#            print(spaceadd)
#            revisexml = i.ljust(spaceadd)
        tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcpsocket.connect((outbound_server_ip,outbound_server_port))
        lengthresp=len(xmlrequest3)
        lengthrespdiff=length-len(str(lengthresp))
        fillregvalue=str(lengthresp).zfill(length)
        finalrequest=fillregvalue+xmlrequest3
        print("SNR request %s" %finalrequest)
        
        req = tcpsocket.send(finalrequest)
        resp = tcpsocket.recv(6024)
        print("SNR response %s" %resp)

   except Exception,error:
       print("Exception occured %s" %error)

xml_receive()
time.sleep(600)

