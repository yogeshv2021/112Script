#!/usr/bin/python

import os
import socket
from time import sleep
import re
import datetime
import subprocess
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import *
import sys
from lxml import *
import threading
from threading import Thread
import logging
import Queue
import time
import itertools 
from itertools import islice
from multiprocessing import Pool


path = "/opt/product/YOGESH/"
filename = "Content.xml"
host = "192.168.151.91"
port = 4080
xmlpath = "".join(path + filename)
numberofapi = 3

class mythread(threading.Thread):

    config_list = []
    app_api_final_request = []
    api_dup = []


    def __init__(self,name):

        threading.Thread.__init__(self)

        self._name = name
        self.lock  = threading.Lock()
        self.xmlpath = xmlpath
        self.numberofapi = numberofapi 
        self.tree = ET.parse(xmlpath)
        self.root = self.tree.getroot()
        self.primary_var = []
        self.trans_var = []
        self.trans  = []
        self.app_api_initial_request =[]

    def run(self):
        print("starting." + self.name)
        self._name(self)
        print("exiting." + self.name)


def retrivexmldata(self):

        self.counter = 0
        self.app_api_len = 0

        while(self.counter < (self.numberofapi)):

            print(self.counter,self.numberofapi)

            self.product_name = self.root.find('PRODUCT').attrib['NAME']
            self.product_name_element = self.root.findall('PRODUCT')

            for self.prod_name in self.product_name_element:
  
                for self.server in self.prod_name.findall('SERVER'):
 
                    self.server_ip = self.server.attrib['NAME']
                    self.server_port = self.server.attrib['PORT']

                for self.app_server in self.server.findall('APPLICATION'):
                    self.app_name = self.app_server.attrib['NAME']
 
                for self.app_api_server in self.app_server.findall('APPLICATION_API'):

                    self.app_api_name = self.app_api_server.attrib['NAME']
                    self.app_api_len = len(self.app_server.findall('APPLICATION_API'))
                    self.app_api_ent_name = self.app_api_server.findall('API_ENTITY')[0].attrib['NAME']
                    self.app_api_flag_name = self.app_api_server.findall('API_FLAG')[0].attrib['NAME']
                    self.app_api_timeout_name = self.app_api_server.findall('API_TIMEOUT')[0].attrib['NAME']
                    self.app_api_not_name = self.app_api_server.findall('TOTAL_NUMBER_OF_MESSAGES')[0].attrib['NAME']
                    self.app_api_nom_flag_name = self.app_api_server.findall('NUMBER_OF_MESSAGE')[0].attrib['NAME']
                    self.app_api_sleep_name = self.app_api_server.findall('SLEEP_BETWEEN_REQUESTS')[0].attrib['NAME']

                    self.api_dup = [self.app_api_name,self.app_api_ent_name,self.app_api_flag_name,self.app_api_timeout_name,self.app_api_not_name,self.app_api_nom_flag_name,self.app_api_sleep_name]

                    try:

                        self.app_api_value = []
                      
                        for self.app_api_increment in self.app_api_server.findall('INCREMENT'):

                            self.app_api_incre0 = self.app_api_increment.findall("*")[0].tag
                            self.app_api_incre1 = self.app_api_increment.findall("*")[0].attrib['NAME']

#                            print(self.app_api_incre0,self.app_api_incre1)

                            self.app_api_incre2 = self.app_api_increment.findall("*")[1].tag
                            self.app_api_incre3 = self.app_api_increment.findall("*")[1].attrib['NAME']

                            self.app_api_incre4 = self.app_api_increment.findall("*")[2].tag
                            self.app_api_incre5 = self.app_api_increment.findall("*")[2].attrib['NAME']

                            self.app_api_incre6 = self.app_api_increment.findall("*")[3].attrib['NAME']
                            self.app_api_incre7 = self.app_api_increment.findall("*")[4].attrib['NAME']
                            self.app_api_incre8 = self.app_api_increment.findall("*")[5].attrib['NAME']

                            self.app_api_value.extend([self.app_api_incre0,self.app_api_incre1,self.app_api_incre2,self.app_api_incre3,self.app_api_incre4,self.app_api_incre5,self.app_api_incre6,self.app_api_incre7,self.app_api_incre8])

                            self.api_dup.extend([self.app_api_incre1,self.app_api_incre3,self.app_api_incre5])

                            print(self.api_dup)

                            if self.app_api_value[1] !="":

                                for self.counter1 in range(1,int(self.app_api_incre6)+1):
                                    self.app_api_incre9 = int(self.app_api_incre1) + self.counter1
#                                    print(self.app_api_incre0,self.app_api_incre9)

                                for self.counter2 in range(1,int(self.app_api_incre7)+1):
                                    self.app_api_incre10 = int(self.app_api_incre3) + self.counter2
#                                   print(self.app_api_incre2,self.app_api_incre10) 

                                for self.counter3 in range(1,int(self.app_api_incre8)+1):
                                    self.app_api_incre11 = int(self.app_api_incre5) + self.counter3
#                                    print(self.app_api_incre4,self.app_api_incre11)


                        self.app_api_primary_imsi_dup = self.app_api_server.find('PRIMARY_IMSI')

                        if self.app_api_primary_imsi_dup == None:
                            self.api_dup.append("")
                   
                        elif self.app_api_primary_imsi_dup != "":
                            self.app_api_primary_imsi = self.app_api_primary_imsi_dup.attrib['NAME']
#                           self.api_dup.append(self.app_api_primary_imsi)
#                            print(self.app_api_primary_imsi)

                        self.app_api_primary_msisdn_dup = self.app_api_server.find('PRIMARY_MSISDN')
 
                        if self.app_api_primary_msisdn_dup == None:
                            self.api_dup.append("")

                        elif self.app_api_primary_msisdn_dup != "":
                            self.app_api_primary_msisdn = self.app_api_primary_msisdn_dup.attrib['NAME']
#                            self.api_dup.append(self.app_api_primary_msisdn)


                        self.app_api_transactionid_dup = self.app_api_server.find('TRANSACTION_ID')

                        if self.app_api_transactionid_dup == None:
                            self.api_dup.append("")

                        elif self.app_api_transactionid_dup != "":
                            self.app_api_transactionid = self.app_api_transactionid_dup.attrib['NAME']
#                            self.api_dup.append(self.app_api_transactionid)

                    except:
                        print("pass")

                    with open(self.xmlpath,"r") as self.file_open:
                        self.file_read = self.file_open.readlines()

                    for self.line in self.file_read:
  
                        self.reg_output = re.search("<REGISTRATION_REQUEST>",self.line)
                        self.req_output = re.search("<REQUEST>",self.line)
   
                        if self.reg_output != None:
                            self.reg_get = subprocess.Popen(["grep","<REGISTRATION_REQUEST>",xmlpath],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                            self.reg_data = self.reg_get.communicate()[0].strip()
                            self.req_get = subprocess.Popen(["grep","<REQUEST>",xmlpath],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                            self.req_data = self.req_get.communicate()[0].strip()
                             
                            self.reg_pass = self.reg_data.split()[self.counter]
                            self.req_pass = self.req_data.split()[self.counter]

                    self.config_list=[]
                    self.counter = self.counter + 1
                    self.config_list.append([",".join(self.api_dup),self.reg_pass,self.req_pass])

                    pid = os.fork()
                    print(pid)

                    if pid == 0:
                        preparexml(self)
                        sys.exit()


def preparexml(self):

    self.count = 0

    self.len_list = len(self.config_list)

    print(self.config_list)

    for self.parse_xml in self.config_list:
        self.app_api_config_det = self.parse_xml[0].split(",")
        self.app_api_reg_init = self.parse_xml[1]
        self.app_api_req_init = self.parse_xml[2]

        if self.app_api_config_det[2] == "1":
            self.app_api_reg_ent = self.app_api_config_det[1]
            self.app_api_flag_name = self.app_api_config_det[2]
            self.time_out = self.app_api_config_det[3]
            self.total_msg = int(self.app_api_config_det[4])
            self.msg_per_sec = int(self.app_api_config_det[5]) + 1
            self.sleep_bet_req = self.app_api_config_det[6]

            self.primary_imsi = self.app_api_config_det[7]
            self.primary_msisdn = self.app_api_config_det[8]
            self.app_api_transactionid = self.app_api_config_det[9]

            print(self.app_api_value[0],self.app_api_value[1],self.app_api_value[2],self.app_api_value[3],self.app_api_value[4],self.app_api_value[5],self.app_api_value[6],self.app_api_value[7],self.app_api_value[8])

#            print(self.app_api_value0,self.app_api_valueself.app_api_incre6,self.app_api_incre7,self.app_api_incre8)
            
            if self.total_msg:
                   

                self.filltotal1 = 0 
                self.filltotal2 = 0
                self.filltotal3 = 0
                self.count1 = 0 
                self.count2 = 0
                self.count3 = 0
                self.msg = 0 

                while (self.count <= self.total_msg):

    
                    print(self.count,self.total_msg) 

                    for self.app_api_reg_output in etree.XML(self.app_api_reg_init):
   
                        for self.reg_output in self.app_api_reg_output.getiterator("ENTITY_NAME"):
  
                            for self.app_api_reg_count in range(int(self.app_api_nom_flag_name)):
                                  
                                if self.app_api_reg_count == int(self.app_api_nom_flag_name) - 1:

#                                    sleep(int(self.sleep_bet_req))

                                    self.app_api_reg_loop_iter = self.app_api_reg_ent

                                    self.reg_output.text = (self.reg_output.text.replace(self.reg_output.text,str(self.app_api_reg_loop_iter),int(self.app_api_nom_flag_name))).strip()
   
                                self.app_api_reg_parse = etree.fromstring(self.app_api_reg_init)
                           
                                for self.app_api_reg_elem in self.app_api_reg_parse.iter():
    
                                    for self.app_api_reg_child in list(self.app_api_reg_elem):

                                        if self.app_api_reg_child.tag == "ENTITY_NAME":
                                            self.app_api_reg_elem.remove(self.app_api_reg_child)

                                    if self.app_api_reg_elem.tag == "HEADER":
                                        self.app_api_reg_add = etree.SubElement(self.app_api_reg_elem,"ENTITY_NAME")
                                        self.app_api_reg_add.text = self.reg_output.text
                                        self.app_api_reg_disp = etree.tostring(self.app_api_reg_parse).strip()
                                        self.reg_length_data = len(self.app_api_reg_disp)
                                        self.reg_fill_data = str(self.reg_length_data).rjust(9,'0')
                                        self.app_api_reg_output = self.reg_fill_data + self.app_api_reg_disp


                            for row in str(self.filltotal1):

                                """ 1st increment of value """

                                for self.total_count1,self.total_count2,self.total_count3 in itertools.izip_longest(range(int(self.app_api_incre6)),range(int(self.app_api_incre7)),range(int(self.app_api_incre8)),fillvalue=row):

                                    maxvalue = max(int(self.app_api_incre6),int(self.app_api_incre7),int(self.app_api_incre8))

                                    self.loop1_iter = int(self.app_api_value[1]) + int(self.filltotal1)

                                    for self.app_api_req_output in etree.fromstring(self.app_api_req_init):

                                        for self.req_output1 in list(self.app_api_req_output):

                                            if self.req_output1.tag == self.app_api_incre0:

                                                self.req_output1.text = self.req_output1.text.replace(self.req_output1.text,str(self.loop1_iter))
  
                                                self.filltotal1 = self.filltotal1 + 1

                                                self.total_count1 = int(self.total_count1) + 1

                                                self.count1 = self.count1 + 1

                                                if self.filltotal1 == int(self.app_api_incre6):

                                                    self.filltotal1 = 0

                                                elif (self.count1 >= maxvalue + 1 and self.count <= self.total_msg):

                                                    self.count1 = 0
                                                    
                                                    pass

#                                                print("%s %s %s before" %(self.count,self.count2,self.total_msg))

                                                """ 2nd increment of value """

                                                self.loop1_iter1 = int(self.app_api_value[3]) + int(self.filltotal2)
  
                                                for self.app_api_req_output in etree.fromstring(self.app_api_req_init):

                                                    for self.req_output2 in list(self.app_api_req_output):
                                    
                                                        if self.req_output2.tag == self.app_api_incre2:
 
                                                            self.req_output2.text = self.req_output2.text.replace(self.req_output2.text,str(self.loop1_iter1))

                                                            self.filltotal2 = self.filltotal2 + 1

                                                            self.total_count2 = int(self.total_count2) + 1
  
                                                            self.count2 = self.count2 +1 

#                                                            print(self.filltotal2,self.req_output2.text) 

                                                            if self.filltotal2 == int(self.app_api_incre7):

                                                                self.filltotal2 = 0
                                                               
                                                            if (self.count2 >= maxvalue + 1 and self.count <= self.total_msg):

                                                                self.count2 = 0

                                                                pass

#                                                            print("%s %s %s after" %(self.count,self.count2,self.total_msg))
 
                                                            """ 3rd increment of value """

                                                            self.loop1_iter2 = int(self.app_api_value[5]) + int(self.filltotal3)
  
                                                            for self.app_api_req_output in etree.fromstring(self.app_api_req_init):

                                                                for self.req_output3 in list(self.app_api_req_output):
                                    
                                                                    if self.req_output3.tag == self.app_api_incre4:
 
                                                                        self.req_output3.text = self.req_output3.text.replace(self.req_output3.text,str(self.loop1_iter2))

                                                                        self.filltotal3 = self.filltotal3 + 1

                                                                        self.total_count3 = int(self.total_count3) + 1
  
                                                                        self.count3 = self.count3 +1 

                                                                        if self.count3 == int(self.app_api_incre8):

                                                                            self.filltotal3 = 0
                                                               
                                                                        if (self.count3 >= maxvalue + 1 and self.count <= self.total_msg):

                                                                            self.count3 = 0

                                                                            break



                                                                        """ Removing and adding the values to elements """

                                                                        self.app_api_req_parse = etree.fromstring(self.app_api_req_init)


                                                                        for self.app_api_req_elem in self.app_api_req_parse.iter():

                                                                            self.app_api_req_child = self.app_api_req_elem.findall("*")
                                                
                                                                            for self.app_api_req_child1 in self.app_api_req_child:

                                                                                if self.app_api_req_child1.tag == self.app_api_incre0:

                                                                                    self.app_api_req_elem.remove(self.app_api_req_child1)

                                                                                    self.app_api_req_add_1 = etree.SubElement(self.app_api_req_elem,self.app_api_incre0)

                                                                                    self.app_api_req_add_1.text = self.req_output1.text


                                                                        for self.app_api_req_elem in self.app_api_req_parse.iter():

                                                                            self.app_api_req_child = self.app_api_req_elem.findall("*")

                                                                            for self.app_api_req_child2 in self.app_api_req_child:
       
                                                                                if self.app_api_req_child2.tag == self.app_api_incre2:

                                                                                    self.app_api_req_elem.remove(self.app_api_req_child2)

                                                                                    self.app_api_req_add_2 = etree.SubElement(self.app_api_req_elem,self.app_api_incre2)

                                                                                    self.app_api_req_add_2.text = self.req_output2.text


                                                                        for self.app_api_req_elem in self.app_api_req_parse.iter():

                                                                            self.app_api_req_child = self.app_api_req_elem.findall("*")

                                                                            for self.app_api_req_child3 in self.app_api_req_child:
       
                                                                                if self.app_api_req_child3.tag == self.app_api_incre4:

                                                                                     self.app_api_req_elem.remove(self.app_api_req_child3)

                                                                                     self.app_api_req_add_3 = etree.SubElement(self.app_api_req_elem,self.app_api_incre4)
 
                                                                                     self.app_api_req_add_3.text = self.req_output3.text

                                                                                     self.app_api_req_disp = etree.tostring(self.app_api_req_parse).strip() 

                                                                                     self.req_length_data = len(self.app_api_req_disp)

                                                                                     self.req_fill_data = str(self.req_length_data).rjust(9,'0')

                                                                                     self.app_api_req_output = self.req_fill_data + self.app_api_req_disp

                                                                                     self.app_api_initial_request = (self.app_api_reg_output + self.app_api_req_output).strip()

##                                                                                     print("%s before" %(self.total_msg))



                                                                                     if self.count <= self.total_msg:

                                                                                         for self.c1,self.c2 in zip(str(self.msg),[self.app_api_initial_request]):
                                                                                                
                                                                                              if int(self.c1) < self.msg_per_sec - 1:

                                                                                                  self.c3 = self.c2

#                                                                                                  print("%s %s before" %(self.c1,self.total_msg))

                                                                                                  tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

                                                                                                  tcpsocket.connect((host,port))

                                                                                                  tcpsocket.send(self.c3)

                                                                                                  print("%s %s" %(self.c1,self.c3))

                                                                                                  resp = tcpsocket.recv(6025)

                                                                                                  tcpsocket.close()

                                                                                              self.msg = int(self.msg) + 1

                                                                                              if int(self.c1) == self.msg_per_sec -1:

                                                                                                  sleep(int(self.sleep_bet_req))

                                                                                                  self.msg =0

                                                                                     self.count = self.count + 1
  
#                                                                                    print(self.count)


                return (self,self.count)


if __name__ == "__main__":

    t1 = mythread(retrivexmldata)
    t1.start()
    t1.join()

    t2 = mythread(preparexml)
    t2.start()
    t2.join()

    print("\nExecution completed\n")
