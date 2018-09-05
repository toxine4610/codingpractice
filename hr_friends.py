
# hacker rank circle of friends
'''
using depth first search here. if the node is not visited, traverse down, and mark as visited
'''

def dfs(mat, visited, i):
	for j in range(len(Mat)):
		if mat[i][j] == 'Y' and visited[j] == False:
			visited[j] = True
			dfs(mat, visited, j)

def findFriends(mat):
	visited = [False]*len(mat)
	count = 0
	for i in range(len(mat)):
		if visited[i] == False:
			dfs(mat, visited, i)
			count += 1
	return count

# === 

N = int(input("Enter number of conditions: "))
Mat = []
for i in range(N):
	foo = str(input("Enter condition: "))
	x = []
	x = [i for i in foo]
	Mat.insert(i, x)

print("Number of friends = {0}".format(findFriends(Mat)))

