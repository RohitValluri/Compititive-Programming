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

def nth_happy_number(n):

    t = [1,7]
    k = 0

    def happynumber(n):
        #convert negative number to positive
        n=abs(n)
        k = 0
        
        x=list(("".join((i) for i in (str(n)))))
        if (len(x)==1):
            if n in (t):
                l.append(z)
                
        #checking for more than 9
        else:
            for i in range(len(x)):
                s = int(x[i])
                k += s*s
                # print("a",a)
                
            if k==1:
                l.append(z)
                # print(l)
                return z
            else:
                return happynumber(k)
    # print(nth-_happy_number(23))
    l=[]
    i=0
    while (len(l)!=n):
        i+=1
    	z=i
	happynumber(i)
        if len(l)==n:
            return (l[n-1])


