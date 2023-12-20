#https://leetcode.com/problems/trapping-rain-water/
#?? hmm might have to deal with this in layers.
#layers might be hard as height goes up to 10^5
#o(n) method i think
#from two pointers:
#set left pointer at the leftmost position, l where the l+1 index is lower
# right pointer goes until height is higher than the height of l+1 index. calculate height and store.
#repeat with left pointer, except it must be greater than previous position of right pointer.
#issue is we don't know if it is going to go up again. if our little hill is inside a giant valley.

#should not be using for loop
#UNLESS WE USE SOMETHING TO CHECK
# def trap(height):
#     lp=0
#     rp=0
#     maxvol=0

#     pauseloop=0
#     for x in range(len(height)-1):
    

#         if height[x]>height[x+1] and x>=pauseloop:
#             lp=x
#             rp=x+1
            
#             while  rp<len(height)-1 and height[rp]<=height[rp-1]:
#                 #finding next index that is higher than the middle of two pointers
#                 rp+=1
            
#             #calculate how much between
#             minisum=0
#             print(lp,rp)
#             mintowers=min(height[lp],height[rp])
#             for x in range(lp+1,rp):
#                 if height[x]<mintowers:
#                     minisum+=mintowers-height[x]
#             maxvol+=minisum

#             pauseloop=rp
#     return maxvol
            
#neetcode's solution stinky algorithm to find height.
def trap(height):
    l,r=0,len(height)-1
    leftMax,rightMax,=height[l],height[r]
    res=0

    while l<r:
        if leftMax<rightMax:
            l+=1
            leftMax=max(leftMax,height[l])

            res += leftMax-height[l]
        else:
            r-=1
            rightMax=max(rightMax,height[r])

            res += rightMax-height[r]
    return res