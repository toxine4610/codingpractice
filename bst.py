
# time complexity for binary search O(log(n))

def binarysearch(arr, target, first, last):
	if last >= first:
		midpoint  = (first+last)/2
		if arr[midpoint] == target:
			return midpoint
		elif arr[midpoint] > target:
			# search the left hand side
			return binarysearch(arr, target, first ,midpoint-1)
		elif arr[midpoint] < target:
			# search the right hand side
			return binarysearch(arr, target, midpoint+1, last)
		else:
			return -1

# ls = [-2,3,4,5,5,10,11,23]

# first = 0
# last = len(ls)-1

# for i in range(len(ls)):
# 	target = ls[i]
# 	print( binarysearch(ls,target,first,last) )

'''
find duplicates in a list using set
'''

def findDuplicates(ls):
	s = set()
	d = {}

	for j in set(ls):
		d[j] = 1

	for i in range(len(ls)):
		if ls[i] in s:
			d[ ls[i] ] = d[ ls[i] ] + 1
		else:
			s.add(ls[i])
	return d

ls = [1,2,3,3,6,4,1]
print("Element frequencies: {0}".format(findDuplicates(ls)))


################################################################
def isSum(ls, target):
	# returns true if the target list has 
	s = set()
	for i in range(len(ls)):
		if abs(target-ls[i]) in s:
			return True
		else:
			s.add(ls[i])
	return False

ls = [1,4,4,1,2,3]
target = 9
print( isSum(ls,target) ) 

def computeDifference(ls):
	min_running  = ls[0]
	max_running  = 0
	max_diff     = 0
	indMin = 0
	indMax = 0

	for i in range(1, len(ls)):
		# compute the next difference..
		max_running = ls[i] - min_running

		if max_running < 0:
			max_running = 0
		if ls[i] < min_running:
			min_running = ls[i]
			indMin = i
		if max_running > max_diff:
			indMax = i
			max_diff = max_running
	return [max_diff, indMin, indMax]

A = [23171,21011,21123,21366,21013,21367]

diff, indMin, indMax = computeDifference(A)

print("Sell on Day = {0}, Buy on = {1}, Profit = {2}".format(indMax, indMin, diff))
