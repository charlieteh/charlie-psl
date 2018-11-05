# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:29:11 2018

@author: Charles.Teh
"""

crowd = "Y"

guestlist = []

while crowd != "N" :
    guest = input("Guest name please\n")
    guestlist.append(guest)
    crowd = input("Are there more people coming for the party? (Y/N)")
    crowd =str.upper(crowd)

guestlist.sort()

print("These are the people coming to your party.")
for names in guestlist :
    print (names)