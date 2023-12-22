#https://leetcode.com/problems/search-in-rotated-sorted-array/
#i think we can just find the minimum index with min-rotated-sorted-array 
#then take that subarray and do binary search on it.


def search(nums,target):
    n=len(nums)
    l=0
    r=n-1

    minindex=0
    #if rotated n times.
    if nums[0]<nums[n-1]:
        minindex=0 #minindex set to 0 anyways, this spits out the first number to find min.
    else:
        while l<r:
            m=(l+r)//2
            print(l,m,r)
            if nums[m]>nums[l]:
                l=m
            elif nums[m]<nums[l]:
                r=m
            else:
                minindex=r
                break
    
    print(minindex)
    if minindex==0:
        return bsearch(nums,target)#regular binary search in nums
    elif target>=nums[0]:
        sortedsub=nums[0:minindex]
        return bsearch(sortedsub,target)
    
    else:
        sortedsub=nums[minindex:]
        result=bsearch(sortedsub,target)
        if result==-1:
            return -1
        else:
            return result+minindex
        #binary search for it in sortedsub

def bsearch(nums,target):
    lp=0
    rp=len(nums)-1

    if target==nums[lp]:
        return lp
    if target==nums[rp]:
        return rp
    
    while lp<rp:

       
        
        if rp-lp==1 or rp==lp:
            return -1
        
        
        middle=(lp+rp)//2
        if nums[middle]>target:
            rp=middle
        elif nums[middle]<target:
            lp=middle
        else:
            return middle
    return -1