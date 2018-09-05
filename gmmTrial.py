# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 16:19:17 2018

@author: Halassalab-CG
"""

import numpy as np
import matplotlib.pyplot as plt


sig1 = 3
sig2 = 1
mu1 = 5
mu2 = 10


Z = []
for i in range(600):
    x1 = sig1*np.random.randn() + mu1
    x2 = sig2*np.random.randn() + mu2
    if np.random.rand() < 0.3:
        Z.append(x1)
    else:
        Z.append(x2)

plt.hist(Z, bins = 30)