

def dcp49(arr):
	max_so_far, global_max = 0,0
	start, end, s = 0,0,0
	for i in range(len(arr)):
		max_so_far += arr[i]
		if max_so_far < 0:
			max_so_far = 0 
			s = i+1
		elif (global_max < max_so_far ):
			global_max = max_so_far
			start = s
			end = i 
	return global_max, start, end

## test
arr = [34, -50, 42, 14, -5, 86]
global_max, start, end = dcp49( arr )
print("Max = {0}".format(global_max))

arr = [-5, -1, -8, -9]
global_max, start, end = dcp49( arr )
print("Max = {0}".format(global_max))