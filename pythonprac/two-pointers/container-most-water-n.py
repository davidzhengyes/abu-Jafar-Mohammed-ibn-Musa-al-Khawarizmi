#https://leetcode.com/problems/container-with-most-water/
#used little hint from neetcode soln start at both sides.

#move the pointer that has the lower height?    
def maxArea(height):
    n=len(height)
    lp=0
    rp=n-1

    max=0
    while lp<rp:

        vol=(rp-lp)*min(height[lp],height[rp])
        if vol>max:
            max=vol
        
        lefttemp=lp
        righttemp=rp
        if height[lp]<height[rp]:
            while height[lp]<=height[lefttemp] and lp<n:
                lp+=1
            #move left pointer right
        elif height[rp]<=height[lp]:
            print(rp,righttemp)
            while height[rp]<=height[righttemp] and rp>0:
                rp-=1 #move right pointer left
    return max
        #else:
            #pass #move either pointer?
