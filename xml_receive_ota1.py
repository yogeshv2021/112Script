#!/usr/bin/python

import os
import socket
import time
import re

#remote_server_ip = "192.168.151.143"
#remote_server_port = 8122

local_ip = "192.168.151.112"  # Standard loopback interface address (localhost)
local_port = 4004  # Port to listen on (non-privileged ports are > 1023)

length=4

xmlresponse1="0057"
xmlresponse2="<OTARegisterResponse><Code>0</Code></OTARegisterResponse>"

xmlresponse3="0041"
xmlresponse4="<OTAResponse><Code>0</Code></OTAResponse>"

getsleep=60
count=0



def xml_receive(count):
   try:
       s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       s.bind((local_ip, local_port))
       s.listen(10)
       conn,address = s.accept()
       while True:
           data = conn.recv(65535)
           getsession=re.findall('<OTARegisterRequest>.*</OTARegisterRequest>',data)
           getrequest=re.findall('<OTARequest>.*</OTARequest>',data)
           print("getfiled %s" %data)
           if len(getsession)>0:
               getlengthresp=len(xmlresponse2)
               lengthresp=len(xmlresponse2)
               lengthrespdiff=length-len(str(getlengthresp))
               fillregvalue=str(lengthresp).zfill(length)
               slresponse=str(fillregvalue)+xmlresponse2
               print(slresponse)
               conn.sendall(slresponse)
               
           elif len(getrequest)>0:
               getlengthresp=len(xmlresponse4)
               lengthresp=len(xmlresponse4)
               lengthrespdiff=length-len(str(getlengthresp))
               fillregvalue=str(lengthresp).zfill(length)
               slresponse=str(fillregvalue)+xmlresponse4
               if count==0:
                   print("sleeping for %s" %getsleep)
                   time.sleep(getsleep)
#                   conn.sendall(slresponse)
                   count=count+1
               else:
                   print(slresponse)
                   conn.sendall(slresponse)
                   count=count+1
           else:
               print("no data received")

           if not data:
               break


       conn.close()

   except Exception as error:
       print("Exception occured %s" %error)

xml_receive(count)

