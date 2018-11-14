# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:52:11 2018

@author: Charles.Teh
"""
import re

hand = open('data/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    
    
    #non-RegEx method
    if line.find('From:') >= 0 :
        print(line)
    
    
    #RegEx method
    
    #if re.search('From:', line):
    #if re.search('^From:', line):
    #if re.search('^X.*:', line):
    #if re.search('^X-\S+:', line):    
    #    print(line)
    
    #print(re.findall('[0-9]+',line))
    
    if re.findall('[A-Z0-9]+.:', line):    
        print(line)
    