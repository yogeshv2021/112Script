#!/usr/bin/python

b = [1,2,3,4,5,6,7,8,9,10,11,12]
d = (1,2,3,4)
dict = {}
dict['a'] = 'apple'
dict['b'] = 'bat'
dict['c'] = 'cattle'

def function(**kwargs):

    c = b[::-1]
    print(c)
    c.append(13) # append the value
    c.insert(5,33) # insert the value at the index position
    c.pop(5) #removes the element based on the index position
    c.remove(6) # removed the element based on the value
    c[4:5] = 44,55 # replacing the element in the list
    c.extend([1,2]) # extending the list
    d = sorted(c) # sorting the list
    dict['a'] = 'ant'
    dict['b'] = 'bat'
    print(dict.items())
    for key in sorted(dict.keys()):
        print(key,dict[key])

    for arg in kwargs:
         a = "".join(reversed(kwargs[arg]))
         print(a)

z = function(arg1="yogesh",arg2="harish")

print(z)

