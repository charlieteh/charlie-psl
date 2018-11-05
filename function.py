# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:58:19 2018

@author: Charles.Teh
"""

#Create a function to print hello

def printMessage(name):
    print(name + ", " + "Hello there.")
    return

printMessage("Charlie")

def addingNumbers (var1, var2):
    total = var1 + var2
    return total

print(addingNumbers(3,4))

def printinfo(name, age):
    "This prints a passed info into thois function"
    print("Name: ", name)
    print("Age: ", age)
    return ;

printinfo("Charlie", 30)

printinfo(age=28, name="Carlos")