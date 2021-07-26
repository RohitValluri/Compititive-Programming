# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	c = 0
	d = 0
	k = 1
	while k<len(a):
		if(a[k] < a[k-1]):
			c = 1
		elif(a[k] > a[k-1]):
			d = 1	
		k+=1
	if(not c or not d):
		return True
	else:
		return False	

		

print(issorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))		