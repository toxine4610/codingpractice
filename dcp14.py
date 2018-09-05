'''
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''

import numpy as np

def returnPi():
	points_inside = 0
	darts = 10000
	for i in range(darts):
		x = np.random.rand()
		y = np.random.rand()
		if np.sqrt(x**2 + y**2) < 1:
			points_inside += 1
	pi = 4*(points_inside/darts)
	return pi

print("Estimated Pi = {:.3f}".format( returnPi() )