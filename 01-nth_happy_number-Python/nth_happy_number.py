# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)


def ishappynumber(n): 
	# your code goes here
	rem = 0
	sum = 0
	while(n>0):
		rem = n%10
		sum = sum +(rem*rem)
		n = n//10
	# print(sum)
	if(sum==1):
		return True
	elif(sum>9):
		return ishappynumber(sum)
	elif(sum==4):
		return False		
	else:
		return False

def nth_happy_number(n):
    c = 0
    l = 0
    num = 1
    while(c!=n):
        if(ishappynumber(num) == True):
            c+=1
            l = num
        num = num + 1
    return l     
# print(ishappynumber(7))
# print(nthhappynumber(1))
# print(nthhappynumber(2))
# print(nthhappynumber(3))
# print(nthhappynumber(4))
# print(nthhappynumber(5))
# print(nthhappynumber(6))
# print(nthhappynumber(7))
# print(nthhappynumber(8))               


