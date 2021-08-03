# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
    #enters when n>0

    if n>=0:
        n = n%len(s)
        s = s[n:] + s[:n]
        return s
    else:
        n=abs(n)%len(s)
        s = s[len(s)-n:]+s[:len(s)-n] 
        return s



# print(fun_rotatestrings('abcd',  -5))
