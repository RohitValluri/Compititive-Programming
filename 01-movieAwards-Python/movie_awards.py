'''
movieAwards(oscarResults) [10 pts]
Write the function movieAwards(oscarResults) that takes a set of tuples, where each tuple holds 
the name of a category and the name of the winning movie, then returns a dictionary mapping 
each movie to the number of the awards that it won. For example, if we provide the set:
{ 
    ("Best Picture", "The Shape of Water"), 
    ("Best Actor", "Darkest Hour"),
    ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
    ("Best Director", "The Shape of Water"),
    ("Best Supporting Actor", "Three Billboards Outside Ebbing, Missouri"),
    ("Best Supporting Actress", "I, Tonya"),
    ("Best Original Score", "The Shape of Water")
}
the function should return as follows
{ 
    "Darkest Hour" : 1,
    "Three Billboards Outside Ebbing, Missouri" : 2,
    "The Shape of Water" : 3,
    "I, Tonya" : 1
}
'''
from collections import Counter
def movie_awards(oscarResults):
    # Your code goes here...
    l=[]
    for i in oscarResults:
        i=list(i)
        l.append(i)
    li=[]
    count=0
    for j in l:
        if j[1] not in li:
            count+=1   
        li.append(j[1])
        # print("li:",li)
    x = Counter(li)
    return x
    # pass
# print(movie_awards({ 
#     ("Best Picture", "The Shape of Water"), 
#     ("Best Actor", "Darkest Hour"),
#     ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
#     ("Best Director", "The Shape of Water"),
#     ("Best Supporting Actor", "Three Billboards Outside Ebbing, Missouri"),
#     ("Best Supporting Actress", "I, Tonya"),
#     ("Best Original Score", "The Shape of Water")
# }))