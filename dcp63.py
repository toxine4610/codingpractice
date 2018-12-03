'''

This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
'''

def searchRows(M, target):
	Rows = len(M)
	Cols = len(M[0])
	for c in range(Cols):
		x = M[:][c]
		x = ''.join(i for i in x)
		if x == target:
			return True
	return False

def searchColumns(M, target):
	Rows = len(M)
	Cols = len(M[0])
	for r in range(Rows):
		x = M[r][:]
		x = ''.join(i for i in x)
		if x == target:
			return True
	return False

def main(M, target):
	if (searchColumns(M,target) == True):
		print("Found in the Columns")
	elif(searchRows(M,target) == True):
		print("Found in the Rows")
	else:
		print("Not Found")

## test
M = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

main(M, 'MASS')



