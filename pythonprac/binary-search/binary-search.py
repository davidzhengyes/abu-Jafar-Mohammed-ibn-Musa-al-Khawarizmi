#https://leetcode.com/problems/binary-search/

#just testing o(n)
#doesnt time out? 194 ms beating 99.75% what the heck
def searchslow(nums,target):
    for x in range(len(nums)):
        if nums[x]==target:
            return x
        
    return -1


#real solution utilizing the fact array is already sorted.
#o(logn)
def search(nums,target):
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


#binary search w recursion???
    #maybe try recursion later