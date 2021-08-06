# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    ch=set(j for i in lst for j in i)
    m=zip(*lst)
    for i,j in zip(lst,m):
        for c in ch:
            if c not in i or c not in j:
                return False
    return True    
    # pass
print(isLatinSquare([[1,2,3,4],[4,3,2,1],[2,1,4,3],[3,4,1,2]]))
print(isLatinSquare([[4,5,6],[5,6,4],[6,4,5]]))
print(isLatinSquare([[7,8,9],[8,9,7],[9,8,7]]))
