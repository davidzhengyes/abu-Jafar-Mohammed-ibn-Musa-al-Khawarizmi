#https://leetcode.com/problems/subsets/description/
#little bit of recursion i think
#add the value in the index tracker or dont.

def subsets(nums):
  
    res=[]

    
    def subsets_rec(currSubset,n):
     
        if n==len(nums):
            a=[]
            for x in currSubset:
                a.append(x)
            res.append(a)
          
        else:
            b=[]
            for x in currSubset:
                b.append(x)
            subsets_rec(b,n+1)
            c=[]
            for x in currSubset:
                c.append(x)
            c.append(nums[n])
          
            subsets_rec(c,n+1)
            
    
    subsets_rec([],0)

    return res