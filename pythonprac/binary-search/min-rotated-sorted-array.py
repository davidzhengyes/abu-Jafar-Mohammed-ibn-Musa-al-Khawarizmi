#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#find the place where the array breaks

def findMin(nums):
    n=len(nums)

    #if rotated n times.
    if nums[0]<nums[n-1]:
        return nums[0]
    

    l=0
    r=n-1

    while l<r:
        m=(l+r)//2
        print(l,m,r)
        if nums[m]>nums[l]:
            l=m
        elif nums[m]<nums[l]:
            r=m
        else:
            return nums[r]
    return nums[0]