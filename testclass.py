# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:10:18 2018

@author: Charles.Teh
"""

"""

class Test:
    
    def talk(self, msg):
        print(msg)
    def myName(self):
        print ("I am Test...")

obj1 = Test()
obj1.talk("Hi")
obj1.myName()

"""

class Test:

    __name = "Test"

    def __init__(self, name="Object"):
        self.name=name
        
    def talk(self,msg):
        #talkName = "Just Talk"
        print(self.name + ", " + msg)
    
    def myName(self):
        print(self.name + ", I am Test...")

    
    
obj1 = Test()
obj1.talk("Hi")
obj1.myName()

obj2 = Test("Obj2")
obj2.myName()

#print(f"Class Name {Test.name}")
print(f"Obj1 Name {obj1.name}")
print(f"Obj2 Name {obj2.name}")