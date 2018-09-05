

# find the running median of a list.
# sorting is O(nlogn) therefore will be O(n2logn) not efficient.


m = []
for i in range(len(Arr)):
	subArr = Arr[0:i+1]
	if len(subArr) == 1:
		m.append(subArr)
	else:
		maxSub	= max(subArr)
		minSub	= min(subArr)
		if len(subArr) % 2 == 1: 
			# if odd, then the median is the middle value of the sorted list
			# sorting is O(nlogn)
		elif len(subArr)%2 == 0:
			# if even, then the mdian is the average of the middle 2 numbers

		