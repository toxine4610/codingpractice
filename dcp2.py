
'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
''' 

# fastest solution will be to mutiply all elemnts and then divide by i for each i, but this is not feasible 
# the array as 0 elements, this will cause a divide by 0

# slow solution due to nested loops........................
def getProd_v1(arr):
	result = []
	# base cases
	if len(arr) == 0:
		return 0
	elif len(arr) == 0:
		return arr
	else:
		for i in range(0,len(arr)):
			A = []
			excl = {i}
			A = [element for i, element in enumerate(arr) if i not in excl]
			product = reduce((lambda x, y: x * y), A) 
			result.append(product)
		return result

arr = [1,2,3,4,5]
print( "test case 1 = {0}".format(getProd_v1(arr)))

arr = [3,2,1]
print( "test case 2 = {0}".format(getProd_v1(arr)))

# fast solution no nested for loop ..................

def calcProd(arr, index):
	prodLeft = 1
	for i in range(0, index):
		prodLeft *= arr[i]
	prodRight = 1
	for i in range(index+1, len(arr)):
		prodRight *= arr[i]
	return prodRight*prodLeft

def getProd_v2(arr):
	result = []
	for i in range(0, len(arr)):
		result.append( calcProd(arr, i) )
	return result

arr = [1,2,3,4,5]
print( "test case 1 (Fast) = {0}".format(getProd_v2(arr)))

arr = [3,2,1]
print( "test case 2 (Fast) = {0}".format(getProd_v2(arr)))
