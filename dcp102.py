

'''
This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].
'''

def get_contiguous_sum(A, k):
	sum_so_far = dict() # this stores the sums and the indices
	sum_so_far[0] = -1
	L = []
	sum = 0
	for ind, item in enumerate(A):
		sum += item
		sum_so_far[sum] = item
		#check if the accumulated sum has reached the target and get the start of the sum sequence
		# if the sum has not yet been reached, this will return a None
		first = sum_so_far.get(sum - k)
		if first is not None:
			L.append( A[ first  : ind + 1 ] )
	return L
#### test
A = [1,2,3,4,5]
k = 9
print( get_contiguous_sum(A,k) )  

A = [2,1,3,4,5]
print( get_contiguous_sum(A,k)) 
