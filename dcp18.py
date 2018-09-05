# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:00:18 2018

@author: Halassalab-CG
"""

def runningMax(arr, k):
    if len(arr) > 0:
        for i  in range(len(arr)-k+1):
            print("Max = {0}".format( max(arr[0+i:k+i]) ))
    else:
        print("Not an array")
        

A = [10,5,2,7,8,7]
k = 3

runningMax(A, k)
            
            
            
        