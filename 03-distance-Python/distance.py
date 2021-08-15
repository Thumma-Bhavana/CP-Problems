import math
# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.


def fun_distance(x1, y1, x2, y2):
	# your code goes here
	d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return int(d)
# print(fun_distance(0,0,0,-2))