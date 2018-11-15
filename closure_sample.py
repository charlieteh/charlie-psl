# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:25:59 2018

@author: Charles.Teh
"""

#Closure Sample

def make_inc(x):
    def inc(y):
        # x is closed in the definition on inc
        return x + y
    return inc

if __name__ == "__main__":
    inc5 = make_inc(5)
    inc10 = make_inc(10)
    
    print(inc5(5)) #return 10 , 5 + 5
    print(inc10(5)) #return 15, 10 + 5
    
