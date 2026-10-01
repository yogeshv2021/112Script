#!/usr/bin/python

import re
import json

a = [1]
b = ["4","5","6","7"]
c = [3|4|5|7]
test= ['/usr/local/bin/tshark -d tcp.port==7112,http -d tcp.port==5090,http -d tcp.port==7412,http -d tcp.port==7412,http -d tcp.port==5017,http -d tcp.port==8004,http -R "http"', '/usr/local/bin/tshark -d tcp.port==4568,http -d tcp.port==7990,http -d tcp.port==8896,http -d tcp.port==5025,http -d tcp.port==6452,http -d tcp.port==5090,http -d tcp.port==4434,http -d tcp.port==8642,http -R "http"']
d= "20190403114303:RN:1:0:FUL|20190403114303HLRSPA005000001:20190403114112005001|234125000000100|449944842300|44||0|7|0| 20190403124503:RRBS:1:0:SWP|20190403124503HLRSPA005000001:20190403124312005001|234125000000100|449944842300|"

l= "'20190403151354:RN:1:0:FUL','20190403151354HLRSPA005000001:20190403151203005001','234125000000100','449944842300','44','','0','7','0',' | '20190403151354:RN:1:0:FUL','20190403151354HLRSPA005000001:20190403151203005001','234125000000100','449944842300','44','','0','7','0','"

t= l.replace("|",",")
e = d.replace("|",",")
f = e.split(" ")
g = re.split("_","test_spoo_ee")


def func(x):
    test1 = []
    if type(x) in [list]:
        for i in x:
            func(i)
    else:
        test1.extend(str(x))



def func(x):
    for i in x.values():
        if type(i) in [list]:
            z=i[1]
        elif type(i) in [dict]:
            z=i["A"]

y=func({1:[2,3,4],2:[3,4,5],3:{"A":3,"B":4,5:{3:"A",4:"B",5:"C"}}})

a = [1,2,3,4]
b = str(a)[1:-1]
a = []

print(17%3)
