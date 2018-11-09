# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:24:23 2018

@author: Charles.Teh
"""

class Puppy:
    
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    def bark(self):
        print ("I am", self.colour, self.name)
    def __str__(self):
        rep = "Puppy Object\n"
        rep += "name: " + self.name + "\n"
        return rep
   
        

puppy1 = Puppy("Max", "Brown")
puppy1.bark()

puppy2 = Puppy("Ruby", "Black")
puppy2.bark()

print(puppy2.name)
print(puppy2)

print(dir(puppy2))

