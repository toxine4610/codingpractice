import numpy as np
import matplotlib.pyplot as plt

def rand5():
	# generate a random number between 0,5
	return np.random.randint(6)

def rand7():
	a,b = rand5(), rand5()
	n = 5*a+b
	if n >= 21:
		return rand7()
	else:
		return n%7

def rand7v2():
	a,b = rand5(), rand5()
	if b <= 3:
		return a
	elif b == 4:
		if a <=3:
			return 6
		else:
			return rand7v2()
	elif b == 5:
		if a <= 3:
			return 7
		else:
			return rand7v2()


## test
n = []
for i in range(10000):
	n.append(rand7v2())

plt.hist(n)
plt.show()




