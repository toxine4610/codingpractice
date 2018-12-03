'''
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
'''

def nextDirection(direction):
	if direction == "right":
		return "down"
	elif direction == "down":
		return "left"
	elif direction == "left":
		return "up"
	elif direction == "up":
		return "right"

def nextPosition(position,direction):
	if direction == "right":
		return (position[0], position[1]+1)
	elif direction == "left":
		return (position[0], position[1]-1)
	elif direction == "down":
		return (position[0]+1, position[1])
	elif direction == "up":
		return (position[0]-1, position[1])

def shouldChange(M,pos):
	'''
	returns False if r,c are within the bounds,
	if True, then change the direction
	'''
	Rows = len(M)
	Cols = len(M[0])
	r,c  = pos
	isInBoundsR = 0 <= r < Rows
	isInBoundsC = 0 <= c < Cols
	return not isInBoundsC or not isInBoundsR or M[r][c] is None

def main(M):
	numElem = len(M)*len(M[0])
	currentDirection = "right"
	currentPosition = (0,0)
	while numElem > 0:
		r,c = currentPosition
		print(M[r][c])
		# replace printed element with None
		M[r][c] = None
		numElem -= 1
		
		next_Position = nextPosition(currentPosition, currentDirection)
		# if the next position is out of the bounds, then change the print direction,
		# also update the position, to prevent the same element from being printed
		if shouldChange(M, next_Position):
			currentDirection = nextDirection(currentDirection)
			currentPosition  = nextPosition(currentPosition, currentDirection)
		else:
			# keep the same direction
			currentPosition  = next_Position


### Test
M  = [[1,  2,  3,  4,  5],
 	  [6,  7,  8,  9,  10],
 	  [11, 12, 13, 14, 15],
 	  [16, 17, 18, 19, 20]]

main(M)


