# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:53:07 2018

@author: Charles.Teh
"""

# Example 1

"""
import matplotlib.pyplot as plt
    
plt.plot([1,2,3,4,5])
plt.ylabel("Some Significant Numbers")
plt.show()
"""

# Example 2

"""
import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at .2 intervals
t = np.arange(0.,5.,0.2)


#
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.axis ([0,6,0,150]) # x and y
plt.show
"""

#Example 3

import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100,15
x= mu + sigma * np.random.randn(10000)

#the histogramhistogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma-15$') #TeX equations
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()