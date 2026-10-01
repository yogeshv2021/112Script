#!/usr/bin/python

import os
import socket
from time import sleep
import re
import time
import subprocess
import xml.etree.ElementTree as ET
import sys


path = "/opt/product/YOGESH"
filename = 'Content.xml'
finalsenddata = []
host = "192.168.151.91"
port = 4080
xmlpath = "".join(path + filename)

def __init__(self, tag, attrib={}, **extra):
    attrib = attrib.copy()
    attrib.update(extra)
    self.tag = tag
    self.attrib = attrib
    self._children = []

def sendrequest():
    os.chdir(path)
    tree = ET.parse('Content.xml')
    root = tree.getroot()
    for child in root:
        tags = child.tag
        attribute = child.attrib
        Parent = tags
# to fetch the values from the tag
        if Parent == "ENTITY":
           E1 = [a.text for a in root.findall("ENTITY/ENTITY_NAME")]
           print(E1)
        if Parent == "PROVISIONING_INTERFACE":
           E2 = [a.text for a in root.findall("PROVISIONING_INTERFACE/HLR/IPADDRESS")]
           E3 = [a.text for a in root.findall("PROVISIONING_INTERFACE/HLR/IPPORT")]
           E4 = [a.text for a in root.findall("PROVISIONING_INTERFACE/IMG/IPADDRESS")]
           E5 = [a.text for a in root.findall("PROVISIONING_INTERFACE/IMG/IPPORT")]
           print(E2,E3,E4,E5)
        if Parent == "REQUESTS":
           E6 = [a.text for a in root.findall("REQUESTS/API/INTERFACE_NAME")]
           E7 = [a.text for a in root.findall("REQUESTS/API/FLAG")]
           E8 = [a.text for a in root.findall("REQUESTS/API/TIMEOUT")]
           E9 = [a.text for a in root.findall("REQUESTS/API/NAME")]
           E10 = [a.text for a in root.find("REQUESTS/API/XML")]
           E11 = [a.text for a in root.findall("REQUESTS/API/NUMBER_OF_THREADS")]
           E12 = [a.text for a in root.findall("REQUESTS/API/NUMBER_OF_MESSAGE")]
           E13 = [a.text for a in root.findall("REQUESTS/API/SLEEP_BETWEEN_REQUESTS")]
           E14 = [a.text for a in root.find("REQUESTS/API/REQUEST/HEADER")]
           E15 = [a.text for a in root.find("REQUESTS/API/REQUEST/BODY")]
           print(E6,E7,E8,E9,E10,E11,E12,E13,E14,E15)
           if E7 == ["1"]:
               file = open('Content.xml','rb')
               l = file.readlines()
               for i in l:
                   Regreq = re.search("<REGISTRATION_REQUEST>",i)
                   Request = re.search("<REQUEST>",i)
                   if Regreq != None:
                       Regsend = subprocess.Popen(["grep","REGISTRATION_REQUEST",filename],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                       Regdata = Regsend.communicate()[0].strip()
                       Reqsend = subprocess.Popen(["grep","<REQUEST>",filename],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                       Reqdata = Reqsend.communicate()[0].strip()
                       Reglengthdata = len(Regdata)
                       Regfilldata = str(Reglengthdata).rjust(9,'0')
                       Regsendxmldata= Regfilldata + Regdata
                       Reqlengthdata = len(Reqdata)
                       Reqfilldata = str(Reqlengthdata).rjust(9,'0')
                       Reqsendxmldata= Reqfilldata + Reqdata
                       finalsenddata = Regsendxmldata + Reqsendxmldata
                       return(finalsenddata)

                   elif Regreq == "":
                       print("No Registration request present")
           else:
               print("Request flag is disabled %s" %E7)
               sys.exit()

def findall(self,xmlpath,namespaces=None):
    return ElementPath.findall(self,path,namespaces)

def startclient(finalsenddata):
    tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcpsocket.connect((host,port))
    tcpsocket.send(finalsenddata)
    sleep(2)
    resp = tcpsocket.recv(6025)
    tcpsocket.close()

def main():
    branch = findall(self,xmlpath)
    list = sendrequest()
    startclient(list)

main()
