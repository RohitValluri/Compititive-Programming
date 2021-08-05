# topScorer(data) [10 Points]
# Write the function topScorer(data) that takes a multi-line 
# string encoding scores as csv data for some kind of 
# competition with players receiving scores, so each 
# line has comma-separated values. The first value on 
# each line is the name of the player (which you can 
# assume has no integers in it), and each value after 
# that is an individual score (which you can assume is a 
# non-negative integer). You should add all the scores 
# for that player, and then return the player with the 
# highest total score. If there is a tie, return all the 
# tied players in a comma-separated string with the names 
# in the same order they appeared in the original data. 
# If nobody wins (there is no data), return None (not the 
# string "None"). So, for example:

def topScorer(data):
    # Your code goes here...
    if data=='':
        return None
    else:
        l=[]
        l1=[]
        x = data.splitlines()
        # print ("x:",x)
        for j in x:
            # print("j:",j)
            y = j.split(',')
            # print("ybefore",y)
            s = 0
            k={}
            k = y.pop(0)
            # print("k:", k)
            l.append(k)
            # print("l:",l)
            # print("yafter:",y)
            for x in y:
                s+=int(x)
            l1.append(s)
            # print("s:",s)
            # print("l1:",l1)
        s1=set(l1)
        # s2=set(l1)    
        if(len(s1)==1):
            return str(','.join(l))
        else:    
            res = {}
            for key in l:
                for value in l1:
                    res[key] = value
                    l1.remove(value)
                    break
            # print(str(res))
            return (max(res, key=res.get))       
    
    # return ""

# print(topScorer('''\
# Fred,11,20,30 
# Wilma,10,20,30,1
# '''))    

data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
assert(topScorer(data) == 'Fred')

data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
assert(topScorer(data) == 'Wilma')

data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
assert(topScorer(data) == 'Fred,Wilma')

assert(topScorer('') == None)
print("All test cases passed...!")
# Hint: you may want to use both splitlines() and split(',') here!
