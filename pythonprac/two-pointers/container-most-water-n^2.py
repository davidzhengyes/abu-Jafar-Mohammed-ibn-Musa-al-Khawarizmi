#https://leetcode.com/problems/container-with-most-water/
#method ?
#surely you cant go through each combination of two lines.
#maybe find the two greatest at every interval and find the max of that?

#time limit exceeded 52/61 testcases
def maxArea(height):

    gap=1

    n=len(height)
    totalmax=0
    while gap<n:

        lp=0
        rp=lp+gap
        currmax=0
        currmaxX=0
        while rp<n:
            minheight=min(height[lp],height[rp])
            vol=gap*minheight
            if vol>currmax:
                currmax=vol
            lp+=1
            rp+=1
        gap+=1
            
        if currmax>totalmax:
            totalmax=currmax
        
    return totalmax

