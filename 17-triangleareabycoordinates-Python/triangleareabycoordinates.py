# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

def trianglearea(s1, s2, s3):
	if(s1 + s2 <= s3) or (s1 + s3 <= s2) or (s2 + s3 <= s1):
		return 0
	else:
		x = (s1+s2+s3)/2
		area = ((x*(x-s1)*(x-s2)*(x-s3))**0.5)
		return area

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	s1 = ((((x2 - x1)**2) + ((y2 - y1)**2))**0.5)
	s2 = ((((x3 - x2)**2) + ((y3 - y2)**2))**0.5)
	s3 = ((((x1 - x3)**2) + ((y1 - y3)**2))**0.5)
	return trianglearea(s1, s2, s3)