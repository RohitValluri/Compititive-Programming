# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    # Your code goes here...
    x=[]
    if(len(lst)==len(lst[0])):
        for i in range(len(lst)):
            
            for j in range(len(lst)):
                x.append(lst[i][j])
            break
            # print("x:", x)

        for i in range(len(lst)):
            for j in range(len(lst)):
                if(lst[i][j] in x and lst[j][i] in x):
                    continue
                else:
                    return False
        return True    
    
        
    # print("s:",s)
    pass
print(isLatinSquare([[1,3,2,4],[4,3,2,1],[2,1,4,3],[3,4,1,2]]))
print(isLatinSquare([[4,5,6],[5,6,4],[6,4,5]]))
print(isLatinSquare([[7,8,9],[8,9,7],[9,8,7]]))
