# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:02:28 2018

@author: Charles.Teh
"""

def f(x) :
    return x**2
print (f(4))

g = lambda x: x**2
print  (g(5))

def square(x):
    return x**2

print(map(square, range(0,11)))

def fact(x,y):
    return x*y

#print (reduce(fact,range(1,5)))

print(map(lambda x: x**2, range(0,11)))

a=(map(lambda x: x**2, range(0,11)))
for item in a:
    print (item)

