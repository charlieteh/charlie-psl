# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:29:34 2018

@author: Charles.Teh
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import seaborn as sns

#Read csv file
df = pd.read_csv("data\Salaries.csv")

#List First 5 records
print(df.head())

#list 20 reconrds
print(df.head(20))

#List Last 5 records
print(df.tail())

#List datatypes
print(df.dtypes)

#List Column Header
print(df.columns)

#print satistics of dataset
print(df.describe())

#print random sameple of 10 records
print(df.sample(10))

