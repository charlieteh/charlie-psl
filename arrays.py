# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:35:19 2018

@author: Tester
"""

guests = ['first','second','third']

#first item in the list starts with 0
print(guests[0])
print(guests[1])
print(guests[2])

#printing last item in the list
print(guests[-1])

#printing 2nd last item in the list
print(guests[-2])

guests.append('fourth')

guests.remove('second')

#exact match for items in the array and return index value
print(guests.index('second'))
