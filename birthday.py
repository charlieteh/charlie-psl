# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:41:32 2018

@author: Tester
"""

import datetime

birthday = input ("When is your birthday (d/m/Y)? ")
birthdate = datetime.datetime.strptime(birthday, "%d/%m/%Y").date()
#why did we list datetime twice?
#because we are calling the strptime function
#which is part of the datetime class
#which is in the datetime module
print ("Your birth month is " + birthdate.strftime('%B'))

#nextBirthday = datetime.datetime.strptime('20/12/2018', '%d/%m/%Y').date()
currentDate = datetime.date.today()
#If you subtract two dates you get back the number of days between those dates
print (birthdate - currentDate)