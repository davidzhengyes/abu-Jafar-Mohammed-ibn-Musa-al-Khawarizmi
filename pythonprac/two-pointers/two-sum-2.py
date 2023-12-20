#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#method
#have two pointers obviously
#stop whenever greater than the sum
#shmove the pointers.
#remember there is a guaranteed solution.

#can have a continueFrom pointer.
#just see how slow it is if we do o(n^2)

#REALLY SLOW SOLUTION:
#yea timed out.
# def twoSum(numbers,target):
#     for x in range(len(numbers)):
#         for y in range(x+1,x+len(numbers[x+1:])+1):
#             print(x,y)
#             if numbers[x]+numbers[y]==target:
#                 return [x+1,y+1]


#throw a lil binary search in there?
def twoSum(numbers,target):
    lp=0
    rp=len(numbers)-1
    #maybe don tneed left pointer bc for loop
    for x in range(len(numbers)):
        if numbers[x]==numbers[lp] and not x==0:
            lp=x
        
        else:
            y=rp
            print(x,y)
            while y>0 and numbers[x]+numbers[y]>=target:
                if numbers[x]+numbers[y]==target:
                    return [x+1,y+1]
                
                y-=1
                #print(y)
            if numbers[rp]>numbers[y]:
                rp=y+1
            else:
                rp=y
         #logic slightly wrong need to be shifting left instead of right.   
            




