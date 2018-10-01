
'''
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''


def dcp75(arr):
	x = []
	if not arr:
		return 0
	cache = [1]*len(arr)
	for i in range(1, len(arr)):
		for j in range(i):
			if arr[i] > arr[j]:
				cache[i] = max(cache[i], cache[j]+1)
				print( (arr[i], arr[j], cache) )

	return max(cache)

## test
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(dcp75(arr))
