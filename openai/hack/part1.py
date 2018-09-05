

import numpy as np

def solution1(X, y):
    # Type your solution here 
    # Run 10,000 steps of projected gradient descent
    example_w = np.abs(np.random.randn(20))
    example_b = np.random.randn()

    epochs = 10000
    learning_rate=0.0001
    N = len(X)

    for i in range(epochs):
    	y_est = np.dot(X, example_w) + example_b
    	cost  = sum([i**2 for i in y-y_est])/N
    	w_gradient = (-2/N)*sum(X*(y-y_est))
    	b_gradient = (-2/N)*sum(y-y_est)
    	example_w  = example_w - learning_rate*(w_gradient)
    	example_b  = example_b - learning_rate*(b_gradient)
    return example_w, example_b





def solution2(X, y):
# Use fancier method to solve more precisely
    todo







# You can use this generic solution() function to run code. To see the
# console output, press "Run" and click on the test case that appears.
# Your actual implementation should be written under solution1(X, y)
# and solution2(X, y) or any additional helper functions you may define.
def solution():
    # Here's some test data.
    np.random.seed(0)
    X = np.random.randn(100, 20)
    y = np.random.randn(100)

    w_estimate, b_estimate = solution1(X,y)

    print(w)

    assert (w_estimate[:10] >= 0).all()
    loss = np.mean(np.square(np.dot(X,w_estimate) + b_estimate - y))
    print(loss)
    
    # DO NOT EDIT THIS RETURN STATEMENT
    return 0

'''
Present your numerical answers here:
>>> w_estimate
array([1.0568251 , 0.1275016 , 0.35348251, 0.47910739, 0.05265889,
0.83231262, 0.73907764, 1.3197847 , 0.3206359 , 0.85084931,
0.10794964, 0.0510789 , 0.82334923, 0.27725038, 1.09642595,
1.06181321, 0.0157843 , 0.93655612, 0.73266884, 0.10777686])
>>> b_estimate
-0.82276559
>>> loss
8.96612928546235
'''