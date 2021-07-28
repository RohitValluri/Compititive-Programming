# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def fun_recursions_alternatingsum(l):
	

	return sum(l[::2]) - sum(l[1::2])

#print(fun_recursions_alternatingsum([99,56,23,98,45]))
# print(fun_recursions_alternatingsum([1, 2, 3, 4]))	