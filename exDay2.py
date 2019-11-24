

##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Wed Nov 20 10:56:48 2019
#
#@author: owner
#"""
#
###EX1:
x= int(input ("x: \t"))
y= int(input ("y: \t"))
if(x>y): 
    print("The greatest number:", x)
else:
     print("The greatest number:", y)
    
###Ex2:
x= int(input ("input a number: \t"))
for a in range(1, 11):
    print(x,'*',a,'=', x*a)
    
##Ex3: 
for a in range (1,6):
    print("*"*a)
for a in range (4,0,-1):
    print("*"*a)
##Ex4:
print("x")
print("y")
print("z")
print("b")

##Ex5:
print("12")
print("15")
print("18")
print("21")
print("24")

##Ex6:
print("1")
print("2")
print("3")

###Ex7:
x= int(input ("input a number: \t"))
sum=0;
for a in range(0, x):
    sum=sum+a
print(sum)

###Ex8:
x= int(input ("input a number: \t"))
print("Even") if (x%2 == 0) else print("Odd")

###Ex9:
for a in range (0,10):
    for z in range (1,10-a):
        print(" ", end="")
    for y in range (1,a):
        print(y, end="")
    for x in range (a, 0, -1):
        print(x, end="")
    print("\n")
for a in range (8,0, -1):
    for z in range (1,10-a):
        print(" ", end="")
    for y in range (1,a):
        print(y, end="")
    for x in range (a, 0, -1):
        print(x, end="")
    print("\n")

  
###Ex10:
while True:
    try:
        n = int(input("Please enter an integer: "))
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print(n)  

###Ex11:
print("\nError Occurred and Handled")
#

    
