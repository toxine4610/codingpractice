'''

This is your coding interview problem for today.

This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
'''

class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None


def print_level_order(root):
	if root is None:
		return

	queue = []
	queue.append(root)
	print(queue)

	while(len(queue)>0):
		print( queue[0].data )

		# dequeue the first item
		node = queue.pop(0)
		
		# enqueue the next item
		if node.left is not None:
			queue.append(node.left)
		if node.right is not None:
			queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
print_level_order(root)