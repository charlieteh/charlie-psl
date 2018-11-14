# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 11:52:13 2018

@author: Charles.Teh
"""
import sys

first = input("Enter the first number ")
second = input("Enter the second number ")

firstNumber = float(first)
secondNumber =float(second)

try:
    result = firstNumber / secondNumber
    print ( first + " / " + second + " = " + str(result))
except :
    error = sys.exc_info()[0]
    print("I am sorry something went wrong")
    print(error)