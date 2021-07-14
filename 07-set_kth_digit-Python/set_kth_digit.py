# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def fun_set_kth_digit(n, k, d):
	if n>0:
		x=[int(a) for a in str(n)]
		y=x[::-1]
		if(k<len(y)):
			y[k]=d
			z=y[::-1]
			return int("".join([str(i) for i in z]))
		else:
			z=y[::-1]
			l="".join([str(i) for i in z])
			s=int(str(d)+str(l))
			return s
	else:
		n=abs(n)
		x=[int(a) for a in str(n)]
		y=x[::-1]
		if(k>=len(y)):
			z=y[::-1]
			l="".join([str(i) for i in z])
			s=int(str("-")+str(d)+str(l))
			return s		