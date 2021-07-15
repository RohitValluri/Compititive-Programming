# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.


def trianglearea(s1, s2, s3):
	# your code goes here
	if(s1 + s2 <= s3) or (s1 + s3 <= s2) or (s2 + s3 <= s1):
		return 0
	else:
		x = (s1+s2+s3)/2
		area = ((x*(x-s1)*(x-s2)*(x-s3))**0.5)
		return area

