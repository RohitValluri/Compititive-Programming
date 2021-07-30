# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.
from collections import Counter
def areAnagrams(s1, s2):
    # Your code goes here...
    count1 = Counter(s1.lower())
    count2 = Counter(s2.lower())
    if count1 == count2:
        return True
    else:
        return False

assert(areAnagrams("Aba", "BAA")==True)
assert(areAnagrams("bca", "cAb")==True)
assert(areAnagrams("xyz", "yux")==False)
assert(areAnagrams("Acf", "fCa")==True)            
print("All test cases are passed!")
# write your test cases here...