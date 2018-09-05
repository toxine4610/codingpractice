
"""
Created on Sun Jul 29 15:01:19 2018

@author: rvrikhye
"""

import numpy as np

def solution1(X, y):
    # Type your solution here 
    # Run 10,000 steps of projected gradient descent
    example_w = np.abs(np.random.randn(20))
    example_b = np.random.randn()

    epochs = 10000
    learning_rate = 0.0001
    N = len(X)
    
    for i in range(epochs):
#       gradient descent
        y_est = np.dot(X, example_w) + example_b
        error = y_est-y        
        w_gradient = 2*np.dot(X.T, error)/N
        b_gradient = 2*sum(error)/N
        example_w  = example_w - learning_rate*(w_gradient)
        example_b  = example_b - learning_rate*(b_gradient)
    #   satisfy the constraint, which is equivalent of projecting onto
    #   max(W_i, 0) for i = 0:9
        for j in range(10):
            if example_w[j] < 0:
                example_w[j] = 0
    return example_w, example_b


# Here's some test data.
np.random.seed(0)
X = np.random.randn(100, 20)
y = np.random.randn(100)
w_estimate, b_estimate = solution1(X,y)
assert (w_estimate[:10] >= 0).all()
loss = np.mean(np.square(np.dot(X,w_estimate) + b_estimate - y))
print(loss)

'''
Result
Loss = 1.8401411620560386
w_estimate = 
array([ 0.        ,  0.        ,  0.        ,  0.34230842,  0.24149126,
        0.04951418,  0.1118281 ,  0.02094962,  0.06239978,  0.10046008,
        0.61313284, -0.02400045,  0.05532608,  0.28047455,  0.36821693,
        0.13986397,  0.15276907,  0.38199654,  0.00118571,  0.26740605])
b_estimate = 
0.5006305847352174
'''
    

