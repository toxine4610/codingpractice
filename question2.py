

import numpy as np
np.random.seed(100)

def cutRope(N,T):
	# N is the initial length of the rope
	# T is the number of iterations
	S = []
	for i in range(T):
		if N > 1:
			cutPoints = np.random.choice( N-1, 2, replace=False)
			cutPoints.sort()
			R = []
			R.append(cutPoints[0]-0)
			R.append(N-cutPoints[1])
			R.append(cutPoints[1] - cutPoints[0])

			N = np.max(R)
			S.append(N)
	return S

# part a
N  = 64
T = 5
S = cutRope(N, T)
print(S)
print("Mean = {0}".format( np.mean(S)))
print("St. Dev. = {0}".format( np.std(S)))


# part c
N  = 1024
T = 10
S = cutRope(N, T)
print("Mean = {0}".format( np.mean(S)))
print("St. Dev. = {0}".format( np.std(S)))





