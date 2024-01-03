#https://leetcode.com/problems/median-of-two-sorted-arrays/
#I have an idea
#as the problem says must write an alg o(log(m+n)), m,n=length of each array,
# log(m) * log(n)
# wlog need to binary search n for each calculation included in log(m)

#STRATEGY:
#Go through the indices of nums1, 0 to m-1. 
#Binary search in nums1, every time using the calculation of binary searching for that index's value
# in nums2 and seeing what index it is at.


#for the calculation:
#in a merged list of length m+n:
#if the sum of m+n is even: we are looking for index (m+n)/2 and (m+n)/2 -1.
#if the sum of m+n is odd: looking for index (m+n)//2 or alternatively (m+n-1)/2

#or can just find (m+n)//2 as a target and subtract one if needed.

#sometimes this value will be in nums1, or nums2, or sometimes an average in either list.


def findMedianSortedArrays(nums1,nums2):
    m=len(nums1)
    n=len(nums2)

    #remember adjust for even (m+n) later. just search for targetIndex for now.
    targetIndex=(m+n)//2-2

    ml=0
    mr=m-1

    #we are traversing nums1 and checking in nums2
    while ml<mr:
        #remember to check the bounds on ml and mr, both of them are in contention instead of the 
        #between numbers.
        if nums1[ml]==nums1[mr]:
            return nums1[ml]
        if binarySearchIndex(nums1[ml])==binarySearchIndex(nums1[mr]):
            return nums1[ml]
        
        mm=(ml+mr)//2
        #need to have targetIndex-1 or -2 because starts at 0.
        if (m+binarySearchIndex(m))<targetIndex:
            ml=m+1
        elif (m+binarySearchIndex(m))>targetIndex:
            mr=m-1
        else:
            #probably bad practice to do this one
            return 


        #can check if the binarySearchIndex of ml and mr as well and if ml's index+1 and mr's index -1
        # in nums2 are the same.


#to find the index of a given value if it was in the list nums.
        #are there unique values in both lists?
        #no unique value, just sorted list.

#just like koko-bananas, find the minimum index where it could be placed.
        #or maybe return a range of numbers?
        #return min and max index in a tuple.

def binarySearchIndex(nums,target):
    n=len(nums)
    l=0
    r=n-1


    if nums[l]==target or nums[r]==target: #just do the thing return the binary search largest and smallest.
        return (minIndex(nums,target),maxIndex(nums,target))

    while (r-l)>1:
        m=(l+r)//2



        if nums[m]<target:
            l=m
        elif nums[m]>target:
            r=m
        else:
            return (minIndex(nums,target),maxIndex(nums,target))
            #return (binary-search-lowest, binary-search-highest)
            #break it into two smaller lists and then search for the highest instance?
            #cant use the same strategy as in koko as they were searching for the lowest instance.
    
    return r
##first try it without duplicates, without the target being in nums

    
def minIndex(nums,target):
    import math
    n=len(nums)
    l,r=0,n-1
    res=r

    while l<=r:
        k=(l+r)//2

        
        if nums[k]>=target:
            res=min(res,k)
            r=k-1
        else:
            l=k+1
    return res

def maxIndex(nums,target):
    import math
    n=len(nums)
    l,r=0,n-1
    res=0

    while l<=r:
        k=(l+r)//2

        
        if nums[k]<=target:
            res=max(res,k)
            l=k+1
        else:
            r=k-1
    return res

def runTests():
    binarySearchIndex([1,2,3,4,4,5,6,7,8],5)
    binarySearchIndex([1,2,3,4,4,5,5,6,7,8],5)
    binarySearchIndex([1,2,3,4,4,6,7,8],5)  