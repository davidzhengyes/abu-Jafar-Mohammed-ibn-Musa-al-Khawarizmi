#https://leetcode.com/problems/product-of-array-except-self/
#hmm 
#method:
#store in a separate array, where element [i] is the product of 
#   every element up to [i]
#do another array but backwards
#so just run through it and multiply at the end.

def productExceptSelf(nums):
    numlength=len(nums)
    forwardproduct=[]
    backwardproduct=[]
    for x in range(numlength):
        forwardproduct.append(0)
        backwardproduct.append(0)
    
    forwardproduct[0]=nums[0]
    
    for x in range(1,numlength):
        forwardproduct[x]=nums[x]*forwardproduct[x-1]

    backwardproduct[numlength-1]=nums[numlength-1]

    for x in range(numlength-2,-1,-1):
        backwardproduct[x]=nums[x]*backwardproduct[x+1]

    res=[]
    for x in range(numlength):
        if x==0:
            res.append(backwardproduct[x+1])
        elif x==numlength-1:
            res.append(forwardproduct[x-1])

        else:
            res.append(forwardproduct[x-1]*backwardproduct[x+1])
    
        
    return res
