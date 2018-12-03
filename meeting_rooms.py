'''
meeting room problem
'''

def assign_rooms(times):
	start_times = [ (t[0], 1) for t in times ]
	end_times = [(t[1],-1) for t in times]
	events = [ t[1] for t in sorted(start_times+end_times, key = lambda x:x[0])]
	max_rooms = 1
	room = 0
	for event in events:
		room += event
		if room > max_rooms:
			max_rooms = room
	return max_rooms

## test
times = [(1,4), (5,6), (8,9), (2,6)]
print("max rooms required = {}".format(assign_rooms(times)))

def covering(x):
	x.sort(key = lambda x:x[0])
	result = []
	i = 0
	def _is_intersect(x,y):
		return not(x[0]>y[1] or x[1]<y[0])

	while i < len(x):
		this_interval = x[i]
		while i < len(x) and _is_intersect(x[i], this_interval):
			interval = ( max(x[i][0], this_interval[0]), min(x[i][1], this_interval[1]) )
			print(interval)
			i += 1
		result.append(this_interval[1])
	return result

## test 
x = [(0,3),(2,6),(3,4),(6,9)]
print(covering(x))