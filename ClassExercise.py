# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 14:28:37 2018

@author: Charles.Teh
"""

class Dog:
    
    def __init__ (self):
        self.name = []
        self.age = []
    def __setitem__ (self, name, age):
        self.name.append(name)
        self.age.append(age)
    
def get_biggest_number(age):
    oldest_dog_age = max(age)
    print ("The oldest dog here is ", oldest_dog_age, " years old.")
    return

#create empty list
inuage = []

inu1 = Dog()
inu1['Max'] = 6
inuage.append(inu1.age)

inu2 = Dog()
inu2['Bobby'] = 15
inuage.append(inu2.age)

inuUser = Dog()
dog_name = input("Dog's name?\n")
dog_age = int(input("Dog's age?\n"))
inuUser[dog_name] = dog_age
inuage.append(inuUser.age)

#convert inuage nested list into 1-dimension list
list_dog_age =[]
for sublist in inuage:
    for item in sublist:
        list_dog_age.append(item)

get_biggest_number(list_dog_age)      