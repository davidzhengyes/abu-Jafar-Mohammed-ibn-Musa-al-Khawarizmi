#https://leetcode.com/problems/koko-eating-bananas/
#hmmm
#she can eat bananas at any speed between min and max of the height of the piles
#if h=piles.length, k=max(piles), so the largest k value is the largest pile height.
#if h=10^9... do we need a minimum for k? don't think we can assign a general minimum. start at 1?
#between 1 and max, so we can do a little binary search between those.
#nlogn i suppose
#ok i knew that before solution


def minEatingSpeed(piles,h):
    import math
    l,r=1,max(piles)
    res=r

    while l<=r:
        k=(l+r)//2
        hours=0
        for p in piles:
            hours+=math.ceil(p/k)
        
        if hours<=h:
            res=min(res,k)
            r=k-1
        else:
            l=k+1
    return res


#yea idk i was close
# def minEatingSpeed(piles,h):
#     small=1
#     big=max(piles)

#     #first check if answer is small or big
#     #if hoursNeeded(piles,big)==h: #cant return big here as could have smaller value in same time.
#         #return big
#     if hoursNeeded(piles,small)==h: 
#         return small
    
#     while (big-small)>1:
        
#         middle=(big+small)//2
#         middleHours=hoursNeeded(piles,middle)
#         smallHours=hoursNeeded(piles,small)
#         bigHours=hoursNeeded(piles,big)
#         print(small,middle,big,middleHours)
#         if smallHours==h:
#             return small
#         elif middleHours<h: #cannot return middle here, smaller value might also ==h.
#             big=middle
#         else:    #ohh just throw a min in there cuz u will be going across the minimum value at some point, 
#                 #and keep going until one smaller than other.
#             small=middle
        
#     print(small,middle,big)
#     print(hoursNeeded(piles,small),hoursNeeded(piles,middle),hoursNeeded(piles,big))
#     return small


# def hoursNeeded(piles,k):
#     import math
#     count=0
#     for x in piles:
#         count+=math.ceil(x/k)

#     return (count)
