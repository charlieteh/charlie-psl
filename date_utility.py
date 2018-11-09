# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:24:29 2018

@author: Tester
"""

import datetime

currentDate = datetime.date.today()
#strftime allows you to specify the date format
print (currentDate.strftime("Please attend our event %A, %B %d in the year %Y"))

currentDate = datetime.date.today()
#timedelta allows you to specify the time to add or subtract  from a date

print ("Timedelta 15 days : ")
print(currentDate + datetime.timedelta (days=15))
