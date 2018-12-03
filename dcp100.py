'''
This problem was asked by Google.

You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
'''
import math

def get_max_dist(pt1,pt2):
	x1,y1 = pt1
	x2,y2 = pt2
	# calculate the taxicab distance between point1 and point2, return the maximum of the vert and horiz distances
	# is because 1 move away between within the unit circle centered on pt1
	dist = max( abs(x2-x1), abs(y2-y1) )
	# this is because the agent can move {0,+1,-1} and stay within the range of one move
	return dist


def number_of_moves(seq):
	max_dist = 0
	for i in range(1,len(seq)):
		max_dist += get_max_dist( seq[i-1], seq[i] )
	return max_dist

### test
seq = [(0, 0), (2, 1), (3, 3)]
print("max number of moves = {}".format(number_of_moves(seq)))
