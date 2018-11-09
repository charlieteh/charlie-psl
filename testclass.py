# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:10:18 2018

@author: Charles.Teh
"""

class Test:
    
    def talk(self, msg):
        print(msg)
    def myName(self):
        print ("I am Test...")

obj1 = Test()
obj1.talk("Hi")
obj1.myName()