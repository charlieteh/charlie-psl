# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:08:02 2018

@author: Tester
"""

import datetime

currentTime = datetime.datetime.now()

print (currentTime)
print (currentTime.hour)
print (currentTime.minute)
print (currentTime.second)

print (datetime.datetime.strftime(currentTime, '%H:%M'))

# %H Hours (24 hours)
# %l Hours (12 hours)
# %p AM or PM
# %m Minutes
# %S Seconds
       