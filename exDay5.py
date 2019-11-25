#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:20:16 2019

@author: owner
"""

class Employee ():
    
    def __init__(self, number:int, name:str, address:str, salary:float, job:str):
        self.number = number
        self.__name = name
        self.__address = address
        self.__salary = salary
        self.__job = job 
        
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    def setAddress(self, newAddress):
        self.__address = newAddress
        
    def getSalary(self):
        return self.__salary
    
    def getJob(self):
        return self.__job
    
    def info1 (self):
        print("\t", "* Employee number:", self.number)
        print("\t", "* Name:", self.getName()) 
        print("\t", "* Address:", self.getAddress()) 
        print("\t", "* Salary:", self.getSalary())
        print("\t", "* Job Title:", self.getJob())
        
    def info2 (self):
        print( "Employee number =", self.number, end=",")
        print( "Name =", self.getName(), end=",") 
        print( "Address =", self.getAddress(), end=",") 
        print( "Salary =", self.getSalary(), end=",")
        print( "Job Title =", self.getJob())
    
    def __del__( self ): 
        print (self.__name, 'has been deleted')
        
        
emp1 = Employee(1, "Mohammad Khalid", "Amman, Jordan", 500, "Consultant")
emp2 = Employee(2, "Hala Rana", "Aqaba, Jordan", 750, "Manager")


print("Employee1 Information:")
emp1.info1()

print("\n")

print("Employee2 Information : ", end="")
emp2.info2()

print("\n")

emp1.setAddress("USA")
print("Employee1 New Address : ", end ="")
print(emp1.getAddress())

print("\n")

del emp1
del emp2       