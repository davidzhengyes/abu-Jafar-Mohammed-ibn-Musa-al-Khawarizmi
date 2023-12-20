#https://leetcode.com/problems/3sum/
#maybe o(n^2) is fine as input is small
#also shmove two pointers and third one might have to go through n list.
#only going in the right direction? as left combinations have already been checked.
#just one level above a twosum?
#no there are repeated calculations

#idk duplicates.
#i tried sorting, but if you have -1 -1 and 2 u cant just remove duplicates?
#ohh hint from neetcode solution, just avoid having it in the same position.
#zamn should have twosum2 repeated after the initial loop.
def threeSum(nums):
    xvisited=set()
    nums=sorted(nums)
    print(nums)

    res=[]
    for x in range(len(nums)-2):
        if nums[x] in xvisited:
            pass
        elif nums[x]>0:
            break

        else:
            xvisited.add(nums[x])
            yvisited=set()
            for y in range(x+1,len(nums)-1):
                #print(x,y)
                rest=set(nums[y+1:])
                if (-1*(nums[x]+nums[y])) in rest and nums[y] not in yvisited:
                    print(x,y)
                    res.append([nums[x],nums[y],(-1*(nums[x]+nums[y]))])
                    yvisited.add(nums[y])
    return(res)

