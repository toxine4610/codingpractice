'''
This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
'''

import numpy as np
def max_cost_path(cost):
	num_rows, num_cols = len(cost), len(cost[0])
	tc = np.zeros_like(cost)
	
	for r in range(1, num_rows):
		tc[r][0] = tc[r-1][0] + cost[r][0]
	for c in range(1, num_cols):
		tc[0][c] = tc[0][c-1] + cost[0][c]
	tc_min = tc.copy()
	for r in range(1,num_rows):
		for c in range(1, num_cols):
			tc[r][c] = max( tc[r-1][c], tc[r][c-1] ) + cost[r][c]
			tc_min[r][c] = min( tc_min[r-1][c], tc_min[r][c-1] ) + cost[r][c]
	return tc[num_rows-1][num_cols-1], tc_min[num_rows-1][num_cols-1]


cost = [[0,3,1,1],
		[2,0,0,4],
		[1,5,3,1]]
print(max_cost_path(cost))
print('\n')

cost = [[0,2,3],
        [5,4,9],
        [6,7,1]]
print(max_cost_path(cost))