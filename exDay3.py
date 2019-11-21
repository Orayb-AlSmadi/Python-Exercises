#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:51:35 2019

@author: owner
"""
list=[1,20,-1,0,1000]
#EX1:
for x in list:
    print(x)

#EX2:
print(sum(list))

#EX3:
print(max(list))

#EX4:
x= set(list)

#EX5:
print("Empty") if (len(list)==0) else print("Not Empty")

#EX6:
tuple=(1,2,3,"Hi", ["B","Y","E"])

for x in tuple: 
    print(x)

#EX7:
num_set = set([0, 1, 2, 3, 4, 5])
for x in num_set:
    print(x)

#EX8:
s1={1,2,3,4,5,6}
s2={2,4,6}
print ( s1 & s2 ) 

#EX9:
print({"green","blue","yellow"})

#EX10:
print(6)

#EX11:
print({1:10, 2:20, 3:30, 4:40, 5:50, 6:60})

#EX12:
print("e")
print("llo,")
print("orl")
print(13)
print("hello, world!")
print("Jello, World!")