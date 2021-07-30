# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isprime(n):
    if n==2:
        return True    
    for i in range(2, n//2):
        if(n%i==0):
            return False
    else:
        return True
        
def repeatsum(n):
    q=0
    f=0
    while(n!=0):
        f=n%10
        q+=f
        n=n//10
    if(q>9):
        return repeatsum(q)
    else: 
        return q        
            
def smith(n):
    if(isprime(n)!=True):
        k = n
        factors = []
        sumoffactors=0
        sumofnumbers=0
        rem=0
        srem = 0
        stotal = 0
        x =0
        z =0
        ve = 0
        ro = 0
        for i in range(2,(n//2) + 1):
            if(isprime(i)==True) and (n%i==0):
                factors.append(i)
        
        for an in str(n):
            ro+=int(an)
            # ro+=an        
        # print("sumofnumbers:",sumofnumbers)
        # while(sumofnumbers!=0):
        #     x=sumofnumbers%10
        #     z+=x
        #     sumofnumbers=sumofnumbers//10
        # print("z:",z) 
        li=[]
        for i in factors:
            
            while (k%i==0 and k!=0):
                li.append(i)    
                sumoffactors+=i
                k=k//i
        e = 0        
        for j in li:
            if(j>9):
                for d in str(j):
                    e+=int(d)
                break    
            e+=j
            
                    
            # print("sumoffactors:",sumoffactors)
        # while(sumoffactors!=0):
        #     srem=sumoffactors%10
        #     stotal+=srem
        #     sumoffactors=sumoffactors//10
        # print("stotal:",stotal)
            
        if(ro==e):
            return True
        else:
            return False
        
        
def fun_nth_smithnumber(n):
    count=0
    ev=1
    re = 0
    while(n!=count):
        if(smith(ev)==True):
            count+=1
            re = ev
        ev+=1
    return re
            

# print(fun_nth_smithnumber(4))
# print(smith(58))
# print(smith(85))
# print(smith(22))
# print(smith(27))
# print(smith(13))
# print(smith(2))
# print(smith(15))
# print(smith(11))
# print(smith(57))
# print(smith(105))

            
            

print(fun_nth_smithnumber(1))
print(fun_nth_smithnumber(2))
print(fun_nth_smithnumber(3))
print(fun_nth_smithnumber(4))
print(fun_nth_smithnumber(5))
print(fun_nth_smithnumber(6))
print(fun_nth_smithnumber(7))
print(fun_nth_smithnumber(8))
print(fun_nth_smithnumber(9))
print(fun_nth_smithnumber(10))
# print(smith(58))
# print(smith(85))
# print(smith(22))
# print(smith(27))
# print(smith(13))
# print(smith(2))
# print(smith(15))
# print(smith(11))
# print(smith(57))
# print(smith(438))
# print(smith(483))
# print(smith(481))
            

            

            

                  