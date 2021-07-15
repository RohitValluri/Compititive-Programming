# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	for i in range(street+1):
		a = i*8
		b = (i+1)*8
		if(abs(street-a)<=8 and abs(street-b)<=8):
			if((abs(street-a) > abs(street-b))):
				return b
			elif((abs(street-a) == abs(street-b)) or (abs(street-a) < abs(street-b))):
				return a
