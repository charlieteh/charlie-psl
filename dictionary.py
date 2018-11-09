# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:43:50 2018

@author: Charles.Teh
"""

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names :
    if name not in counts:
        counts[name] =1
    else:
        counts[name] = counts[name]+1

print(counts)

# use .get to obtain count figure by specifying the 'name' or name
print(counts.get('csev',0))
