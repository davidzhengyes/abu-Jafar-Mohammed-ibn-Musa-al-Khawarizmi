import math
import time
import random
import sys

def mergesort(lst):
    middle=math.floor((len(lst)+1)/2)

    sublst1=lst[0:middle]
    sublst2=lst[middle:len(lst)]
    ##probably both these conditions not needed due to math.
    if (len(sublst1)==0) or (len(sublst2)==0):
        return sublst1+sublst2
    else:
        return merge(mergesort(sublst1),mergesort(sublst2))

    
    


def merge(sortedlist1, sortedlist2):

#first check if we have empyt list because can't call [0] on empty
    if len(sortedlist1)==0:
        return sortedlist2
    elif len(sortedlist2)==0:
        return sortedlist1
    
    s1=sortedlist1[0]
    s2=sortedlist2[0]

    if s1<s2:
        return [s1]+merge(sortedlist1[1:len(sortedlist1)],sortedlist2)
    elif s2<s1:
        return [s2]+merge(sortedlist1,sortedlist2[1:len(sortedlist2)])
    else:
        return [s1]+[s2]+merge(sortedlist1[1:len(sortedlist1)],sortedlist2[1:len(sortedlist2)])



randomlist=[]
for x in range(1000):
    randomlist.append(random.randint(0,10000))

t1=time.time()
print(mergesort(randomlist))
print(time.time()-t1) 
print(sys.getrecursionlimit())