'''
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.

'''

# solve recursively, O(logN)
def pow(x,y):
	if y == 0: 
		return 1
	temp = pow(x,y/2)
	if (y%2 == 0):
		return temp*temp
	else:
		if (y > 0):
			return x*temp*temp
		else:
			return (temp*temp)/x
base = 2
for i in range(0, 11):
	print("{0}^{1} = {2}".format(base, i, pow(base, i)))