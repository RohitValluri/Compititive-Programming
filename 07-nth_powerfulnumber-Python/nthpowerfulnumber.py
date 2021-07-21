# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def factors(n) :
    i = 1
    while i <= n :
        if (n % i==0) :
            print (i)
        i = i + 1
# print(factors(100))
def isprime(n):
  if n > 1:  
   for i in range(2,n):  
       if (n % i) == 0:    
           break  
   else:  
       return n 
	   
def nthpowerfulnumber(n):
	# Your code goes here
	pass
