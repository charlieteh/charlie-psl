# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:50:34 2018

@author: Charles.Teh
"""

class Critter:
    """A virtual pet"""
    def talk(self):
       print ("Hi, I'm an instance of class Critter.") 
       
crit = Critter()
crit.talk()