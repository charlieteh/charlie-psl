# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:37:32 2018

@author: Charles.Teh
"""

import numpy as np

x = np.float32(1.0)
print(x)

y = np.int_([1,2,4])
print(y)

z = np.arange(3,dtype=np.uint8)
print(z)

c = np.arange(9).reshape(3,3)
print(c)

x = np.arange(10)
print(x[2:5])
print(x[:-7])