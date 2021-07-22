# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def fun_nth_additive_prime(n):
	n=n+1
	#check the given number is an additive prime or not
	def isadditiveprime(n):
		k=0
		if n==1:
			return False
		elif n==2:
			list1.append(n)
			return True
		for i in range(2,(n//2)+1): 
			if n%i==0:              # checking for prime numbers above 2
				return False
		
		for i in (str(n)): # iterating in the given number and adding up each digits
			k+=int(i)
		
			
		for i in range (2,k):
			if k%i==0:
				return False
		list1.append(n)
		return True
	# condition to find out the nth additive prime
	num=0
	list1=[]
	while (len(list1)!=n):
		num+=1
		isadditiveprime(num)
		if (len(list1)==n):
			return (list1[n-1])
