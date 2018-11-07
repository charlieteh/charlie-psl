# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:00:59 2018

@author: Charles.Teh
"""

import csv

myCSVfile = open('data/demo.csv','r')
dataFromFile = csv.reader(myCSVfile)

print(dataFromFile)

"""
with open(fileName, accessMode) as myCSVfile:
    #Read the file contents
    dataFromFile = csv.reader(myCSVfile)
    #For loop that will run once per row
    for row in dataFromFile:
        print(row)
"""

for row in dataFromFile:
    print(row)
    
myCSVfile.close()