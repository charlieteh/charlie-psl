# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:18:09 2018

@author: Tester
"""

answer = input ("Would you like express shipping? (Yes or No)").lower()
if answer == "yes" :
    print ("That will be an extra $10")
    shippingSelected == True
else :
    print ("Standard shipping selected.")
    shippingSelected == False
    


if(shippingSelected):
    print ("Thank you for selecting Express shipping")


deposit = input ("How much would you like to deposit? ")
if int(deposit) > 100:
    print ("You get a free toaster!")
else :
    print ("Enjoy your mug!")
print ("Have a nice day")