# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.
from collections import Counter, OrderedDict
def mostfrequentdigit(n):
	# your code goes here
	n=str(n)
	count = Counter(n)
	return int(max(count, key=count.get))
	# pass
# x = (input())
# print(mostfrequentdigit(x))