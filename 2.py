#!/usr/bin/python
# To Print the prime numbers below 100

k=[]
n=20
if n>1:
    for i in range(10,n):
        for j in range(2,i):
            if (i%j)==0:
                break
            elif (i%j)!=0:
                pass
        else:
            pass

# to print factorial of numbers
z=1
for i in range(1,6):
    for j in range(i):
         print("* ",end='')
    print("\r")