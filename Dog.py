# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:05:41 2018

@author: Charles.Teh
"""

class Dog:
    
    # Class Attributes
    species = 'mammal'
    
    # Initializer / Instance Attributes
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
        
# Instantiate the Dog object
jake = Dog("Jake", 7)
doug = Dog("Doug", 4)
william = Dog("William", 10)

# Determine the oldest dog

def get_biggest_number(*args):
    return max(args)

print ("The oldest dog is {} years old.".format(get_biggest_number(jake.age,doug.age,william.age)))

#print(jake.species)