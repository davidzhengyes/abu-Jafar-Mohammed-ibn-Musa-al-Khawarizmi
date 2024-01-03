#https://leetcode.com/problems/subsets-ii/description/
#ain't it just subsets but remove duplicates? Can remove duplicates in o(n) time?
#hah not that simple can't put a list in a hashset.

# def subsetsWithDup(nums):
  
#     res=[]
#     nums.sort()
#     #this is really stupid. I don't think the input array should be sorted.
#     #I think the people who wrote testcases got it slightly wrong.


#     #INSTEAD OF USING THE LOOP TO TRANSFER THE LIST:
#     #USE LIST.COPY()
#     def subsets_rec(currSubset,n):
     
#         if n==len(nums):
#             a=[]
#             for x in currSubset:
#                 a.append(x)
#             if a not in res:
#                 res.append(a)
          
#         else:
#             b=[]
#             for x in currSubset:
#                 b.append(x)
#             subsets_rec(b,n+1)
#             c=[]
#             for x in currSubset:
#                 c.append(x)
#             c.append(nums[n])
          
#             subsets_rec(c,n+1)
            
    
#     subsets_rec([],0)
#     return res
   
    
    #neetcode solution, just testing speed
#maybe faster using copy
#maybe faster using pop instead of making all these extra arrays.
#same time complexity though.
def subsets(nums):
    res=[]
    subset=[]

    def dfs(i):
        if i>=len(nums):
            res.append(subset.copy())
            return
        
        subset.append(nums[i])
        dfs(i+1)
        subset.pop()

        dfs(i+1)

    dfs(0)
    return res
