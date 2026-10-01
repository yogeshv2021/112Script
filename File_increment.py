#!/usr/bin/python

incremvalue='AAA-AAAAAA'

count=0

for i in range(0,100):
    for j in range(0,10):
        for count in range(0,26):
            if incremvalue[j] == "-":
                l = incremvalue[j]
            else:
                l=chr(ord(incremvalue[j]) + count)
            if j >0:
                k=incremvalue[0:j] + l + incremvalue[j+1:]
            else:
                k=l + incremvalue[j+1:]
            print(k,i)
            count = count +1

