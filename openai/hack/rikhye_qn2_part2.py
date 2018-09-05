#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 16:09:30 2018

@author: rvrikhye
"""

import numpy as np

def computeError(X, example_w, example_b):
    y_est = np.dot(X, example_w) + example_b
    # cost  = sum([i**2 for i in y_est-y])/N
    error = y_est-y
    return [y_est, error]

def solution2(X, y):
    
    # perform ordinary least squares
    const = np.ones((100,1))
    Xn = np.column_stack((const, X))
    
    Wls = np.matmul( np.linalg.inv(np.matmul(Xn.T,Xn)), Xn.T )
    W_hat = np.matmul(Wls, y)
    
    example_b = W_hat[0]
    example_w = W_hat[1:]
    
    print(example_w)
    
    y_est, error = computeError(X, example_w, example_b)
    
    # following Baram IEEE 1980, the MMSE under a linear constraint is 
    # the linear sum of the unconstrained estimate and the constraint.
    # in this case the constaint is max(W_i, 0) for i = 0:9
    # i think what i have to use here is the Lawson-Hanson active set method 
    
    
    return example_w, example_b
    

# Here's some test data.
np.random.seed(0)
X = np.random.randn(100, 20)
y = np.random.randn(100)
w_estimate, b_estimate = solution2(X,y)
assert (w_estimate[:10] >= 0).all()
loss = np.mean(np.square(np.dot(X,w_estimate) + b_estimate - y))
print(loss)