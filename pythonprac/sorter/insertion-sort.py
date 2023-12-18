import random
import time
def insertionSort (unsortlist):
    if len(unsortlist)==1:
        return unsortlist
    x=len(unsortlist)-2
    n=len(unsortlist)
    while x>=0:
        unsortlist[x:n]=insert(unsortlist[x],unsortlist[x+1:n])
        x-=1
    return unsortlist
    


def insert (n, sortedlist):
    x=0
    while x<len(sortedlist):
        if sortedlist[x]>=n:
            sortedlist.insert(x,n)
            break
        x+=1

    if x==(len(sortedlist)):
        sortedlist.append(n)

    return sortedlist


randomlist=[]
for x in range(1000):
    randomlist.append(random.randint(0,10000))

t1=time.time()
insertionSort(randomlist)
print(time.time()-t1) 