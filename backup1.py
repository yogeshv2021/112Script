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
from lxml import etree
import threading
from threading import Thread
import logging
import Queue
import time
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
        self.xmlpath = xmlpath
        self.numberofapi = numberofapi 
        self.tree = ET.parse(xmlpath)
        self.root = self.tree.getroot()
        self.primary_var = []
        self.trans_var = []
        self.trans  = []

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
                    self.app_api_numberofseries = self.app_api_server.findall('NUMBER_OF_SERIES')[0].attrib['NAME']

                    self.api_dup = [self.app_api_name,self.app_api_ent_name,self.app_api_flag_name,self.app_api_timeout_name,self.app_api_not_name,self.app_api_nom_flag_name,self.app_api_sleep_name,self.app_api_numberofseries]

                    try:
                        self.app_api_primary_imsi_dup = self.app_api_server.find('PRIMARY_IMSI')


                        if self.app_api_primary_imsi_dup == None:
                            self.api_dup.append("")
                   
                        elif self.app_api_primary_imsi_dup != "":
                            self.app_api_primary_imsi = self.app_api_primary_imsi_dup.attrib['NAME']
                            self.api_dup.append(self.app_api_primary_imsi)

                        self.app_api_primary_msisdn_dup = self.app_api_server.find('PRIMARY_MSISDN')
 
                        if self.app_api_primary_msisdn_dup == None:
                            self.api_dup.append("")

                        elif self.app_api_primary_msisdn_dup != "":
                            self.app_api_primary_msisdn = self.app_api_primary_msisdn_dup.attrib['NAME']
                            self.api_dup.append(self.app_api_primary_msisdn)


                        self.app_api_transactionid_dup = self.app_api_server.find('TRANSACTION_ID')

                        if self.app_api_transactionid_dup == None:
                            self.api_dup.append("")

                        elif self.app_api_transactionid_dup != "":
                            self.app_api_transactionid = self.app_api_transactionid_dup.attrib['NAME']
                            self.api_dup.append(self.app_api_transactionid)

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
                    print(self.config_list)

                    pid = os.fork()
                    print(pid)

                    if pid == 0:
                        preparexml(self)
                        sys.exit()


def preparexml(self):

    self.count = 0

    self.len_list = len(self.config_list)

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
            self.app_api_numberofseries = int(self.app_api_config_det[7]) + 1

            self.primary_imsi = self.app_api_config_det[8]
            self.primary_msisdn = self.app_api_config_det[9]
            self.app_api_transactionid = self.app_api_config_det[10]
            
            if self.total_msg:
                   
                self.count = 0 

                while (self.count <= self.total_msg):

                    print(self.count,self.total_msg)

                    for self.app_api_reg_output in etree.XML(self.app_api_reg_init):
   
                        for self.reg_output in self.app_api_reg_output.getiterator("ENTITY_NAME"):
  
                            for self.app_api_reg_count in range(self.app_api_numberofseries):
                                  
                                if self.app_api_reg_count == self.app_api_numberofseries - 1:

                                    sleep(int(self.sleep_bet_req))

                                    self.app_api_reg_loop_iter = self.app_api_reg_ent

                                    self.reg_output.text = (self.reg_output.text.replace(self.reg_output.text,str(self.app_api_reg_loop_iter),self.app_api_numberofseries)).strip()
   
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

                    for self.app_api_req_output in etree.fromstring(self.app_api_req_init):

                        for self.req_output in list(self.app_api_req_output):

                            for self.total_count in range(self.msg_per_sec):

                                    if self.req_output.tag == "PRIMARY_IMSI":
                                        self.primary_imsi_loop_iter = int(self.primary_imsi) + self.total_count
                                        self.req_output.text = (self.req_output.text.replace(self.req_output.text,str(self.primary_imsi_loop_iter),self.app_api_numberofseries)).strip()
                                        self.primary_var  = self.req_output.text
#                                        print("%s primary imsi" %self.primary_var)

                                        for self.app_api_req_output in etree.fromstring(self.app_api_req_init):
   
                                            for self.req_output1 in list(self.app_api_req_output):

                                                if self.req_output1.tag == "TRANSACTION_ID":

                                                    self.trans_loop_iter = int(self.app_api_transactionid) + self.total_count
                                                    self.req_output1.text = (self.req_output1.text.replace(self.req_output1.text,str(self.trans_loop_iter),self.app_api_numberofseries)).strip()
                                                    self.trans_var  = self.req_output1.text      

                                                    self.app_api_req_parse = etree.fromstring(self.app_api_req_init)

                                                    for self.app_api_req_elem in self.app_api_req_parse.iter():
   
                                                        for self.app_api_req_child in list(self.app_api_req_elem):

                                                            if self.app_api_req_child.tag == "TRANSACTION_ID":
                                                                self.app_api_req_elem.remove(self.app_api_req_child)
 

                                                            for self.app_api_req_child1 in list(self.app_api_req_child):
 
                                                                if self.app_api_req_child1.tag == "PRIMARY_IMSI":
  
                                                                    for self.app_api_req_elem1 in self.app_api_req_elem.findall('BODY'):
                                                                        self.app_api_req_elem1.remove(self.app_api_req_child1)

                                                                        if self.app_api_req_elem1.tag == "BODY":
                                                                            self.app_api_req_primary_add = etree.SubElement(self.app_api_req_elem1,"PRIMARY_IMSI")
                                                                            self.app_api_req_primary_add.text = self.primary_var

                                                        if self.app_api_req_elem.tag == "HEADER":
                                                            self.app_api_req_trans_add = etree.SubElement(self.app_api_req_elem,"TRANSACTION_ID")
                                                            self.app_api_req_trans_add.text = self.trans_var
   
                                                            self.app_api_req_disp = etree.tostring(self.app_api_req_parse).strip()
                                                            self.req_length_data = len(self.app_api_req_disp)
                                                            self.req_fill_data = str(self.req_length_data).rjust(9,'0')
                                                            self.app_api_req_output = self.req_fill_data + self.app_api_req_disp
                                                            self.app_api_initial_request = (self.app_api_reg_output + self.app_api_req_output).strip()

                                                            if self.count <= self.app_api_not_name:
                                                                tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                                                                tcpsocket.connect((host,port))
                                                                tcpsocket.send(self.app_api_initial_request)
                                                                print(self.app_api_initial_request)
                                                                resp = tcpsocket.recv(6025)
                                                                tcpsocket.close()

                                                                self.count = self.count + 1
#                                                            print("%s" %self.count)

    return(self,self.count)


lock  = threading.Lock()

if __name__ == "__main__":

    t1 = mythread(retrivexmldata)
    t2 = mythread(preparexml)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nExecution completed\n")
