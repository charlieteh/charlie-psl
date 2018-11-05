# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:30:43 2018

@author: Charles.Teh
"""

filename = "Sample_char.txt"
accessMode = "w"

myFile = open(filename, accessMode)
myFile.write ("Hi there!,\n")
myFile.write ("How are you?")
myFile.close()
"""

anotherFile = open("demo.csv","r")
fileContent = anotherFile.read()
print (fileContent)

fileContent = anotherFile.readline()
print(fileContent)
"""