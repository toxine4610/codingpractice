'''

Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).

'''

class ExpressionTree:
	def __init__(self, value):
		self.value = value
		self.left  = none
		self.right = none

def isOperator(C):
	if (C == '*' or C == '+' or C = '-'):
		return True
	else:
		return False

def inorder(t):
    if t is not none:
        inorder(t.right)
        print t.value
        inorder(t.right)
