# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

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
	else:
		return False

def isPrime(n):
    if n>1:
        for i in range(2, int(n/2)+1):
            if(n%i==0):
                return False
        else:
            return True
    else:
        return False 

def ishappyprimenumber(n):
    # Your code goes here
    if(ishappynumber(n) and isPrime(n)):
        return True
    return False    
    # pass

print(ishappynumber(833))
# print(isPrime(833))
    