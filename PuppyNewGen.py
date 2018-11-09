# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:29:01 2018

@author: Charles.Teh
"""

class PuppyNewGen:
    
    def __init__(self):
        self.name = []
        self.colour = []
    def __setitem__ (self, name, colour):
        self.name.append(name)
        self.colour.append(colour)    
    def __getitem__(self,name):
        if name in self.name:
            return self.colour[self.name.index(name)]
        else:
            return None
    
dog = PuppyNewGen()
dog['Max']= 'Brown'
dog['Ruby'] = 'Yellow'
print ("Max is", dog ['Max'])
