# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 08:47:54 2018

@author: Halassalab-CG
"""



def makeList(n):
    R = []
    for i in range(1, n+1):
        A = list(range(i))
        R.insert(i, A)
    return R

n = 10
R = makeList(n)
print(makeList(n))
        