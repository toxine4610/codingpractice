


def kadanesAlgorithm(Arr):
	max_so_far = 0
	max_here   = 0
	start = 0
	s = 0
	end = 0

	for i in range(0, len(Arr)):

		max_here += Arr[i]

		if (max_here > max_so_far):
			max_so_far = max_here
			end = i
			start = s

		if (max_here < 0):
			# reset the value:
			max_here = 0
			s = i + 1

		
	return [max_so_far, start, end]

Arr = [-2, -3, 4, -1, -2, 1, 5, -3]
max_so_far, start, end = kadanesAlgorithm(Arr)

print("Sum = {0}, Starts = {1}, Ends {2}".format(max_so_far,start, end))
print( Arr[start:end+1] )