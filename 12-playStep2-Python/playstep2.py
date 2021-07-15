# This is the most complicated part. Write the function playstep2(hand, dice) that plays step 2 as
# explained above. This function takes a hand, which is a 3-digit integer, and it also takes dice,
# which is an integer containing all the future rolls of the dice. For example, if dice is 5341,
# then the next roll will be a 1, then the roll after that will be a 4, then a 3, and finally a 5.
# Note that in a more realistic version of this game, instead of hard-coding the dice in this way,
# we'd probably use a random-number generator.

# With that, the function plays step2 of the given hand, using the given dice to get the next rolls
# as needed. At the end, the function returns the new hand, but it has to be ordered, and the
# function also returns the resulting dice (which no longer contain the rolls that were just used).

# For example:
# assert(playstep2(413, 2312) == (421, 23))
# Here, the hand is 413, and the future dice rolls are 2312. What happens? Well, there are no
# matching dice (pair) in 413, so we keep the highest die, which is a 4, and we replace the 1 and the 3
# with new rolls. Since new rolls come from the right (the one's digit), those are 2 and 1. So the
# new hand is 421. It has to be sorted, but it already is. Finally, the dice was 2312, but we used 2
# digits, so now it's just 23. We return the hand and the dice, so we return (421, 23).

# For Example:
# assert(playstep2(544, 456) == (644, 45))
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# So the output is (644, 45)

# Here are some more examples. Be sure you carefully understand them:
# assert(playstep2(413, 2312) == (421, 23))
# assert(playstep2(413, 2345) == (544, 23))
# assert(playstep2(544, 23) == (443, 2))
# assert(playstep2(544, 456) == (644, 45))
# Hint: You may wish to use handToDice(hand) at the start to convert the hand into the 3 individual
# dice.
# Hint: Then, you may wish to use diceToOrderedHand(a, b, c) at the end to convert the 3 dice back
# into a sorted hand.
# Hint: Also, remember to use % to get the one's digit, and use //= to get rid of the one's digit.

from collections import Counter

def dicetoordered(a, b, c):
    li=[a, b, c]
    li.sort(reverse=True)
    return int("".join(str(i) for i in li))

def handtodice(hand):
    x=[int(i) for i in str(hand)]
    return x
    

def playstep2(hand, dice):
    # your code goes here
    # x = [int(a) for a in str(hand)] #split the hand into a list of individual integers
    x=handtodice(hand)
    a=list(set(x)) #remove duplicate integers

    #case 1 : there are no duplicate integers
    if len(a)==3:
        a.sort(reverse=True) #arrange the list in descending order
        z=str(a[0])
        y=str(dice%10)
        print("y", y)
        q=str((dice%100)//10)
        print("q", q)
        e=(z+y) # last two digits of hand are replaced by the last two digits of dice
        # x=int("".join(sorted(e, reverse=True))) #arrange the string in descending order and convert it into integer
        x = dicetoordered(z, y, q)
        #print("x",x)
        t=dice//100 # the last two digits are sliced from the dice
        #print("t",t)
        c=(x,t)
        print("c", c)
        return c
	#case 2: there are duplicate integers	

    else:
        s=[]
        d=Counter(x) # counter is used to find out the individual count of each integer
        for i in d:
            if d[i]>1:    #if count of any integer is morethan 1 then it will be stored in a seperate string          
                string=str(i)
                g=(string + string)
                print("counter",g)
                y=str(dice%10)
                i=(g+y) #last digit of hand is replaced by the last digit of dice
                k=int("".join(sorted(i, reverse=True)))
                k=dicetoordered()
                print("k",k)
                s=dice//10
                c=(k,s)
                return c

print(playstep2(413, 2312))