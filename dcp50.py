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

def constructTree(postfix):
	stack = []
	for char in postfix:
		if not isOperator(char):
			t = ExpressionTree(char)
			stack.append(t)
		else:
			t = ExpressionTree(char)
			t1 = stack.pop()
			t2 = stack.pop()

			t.right = t1
			t.left  = t2
			stack.append(t)
	t = stack.pop()
	return t

def operators(val):
	# create dictionary
	d = {'plus' : lambda x,y: x+y, 'times' : lambda	x,y: x*y, 
		'minus' : lambda x,y: x-y , 'divide': lambda x,y: x/y}
	return d[val]

def evaluate(root):
	if root.val == 'plus'
		f = operators('plus')
		return f( evaluate(root.left) ,  evaluate(root.right))
	elif root.val == 'minus':
		f = operators('minus')
		return f( evaluate(root.left) ,  evaluate(root.right))
	elif root.val == 'times':
		f = operators('times')
		return f( evaluate(root.left) ,  evaluate(root.right))
	elif root.val == 'divide':
		f = operators('divide')
		return f( evaluate(root.left) ,  evaluate(root.right))
