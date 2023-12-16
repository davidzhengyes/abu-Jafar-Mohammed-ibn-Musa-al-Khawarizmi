#https://leetcode.com/problems/two-sum/
#blyat
#hopefully n^2 works.
#try n^2 then later try optimize
#after watching the first 44 seconds of neetcode's video
#he says the intuitive method: which is what i've done, is to check every combination of two values.
#realized that there could well be duplicates in the dataset. use hashset to check if already checked.
#the else should not be there lol 2183ms run.
#didnt make faster?



# def twoSum (nums, target):
#     checked=set()
#     for x in range(len(nums)):
#         if x not in checked:
#             for y in range(x+1,len(nums)):
#                 if (nums[x]+nums[y])==target:
#                     return [x,y]
#         else:   
#             checked.add(x)
        
def twoSum (nums,target):
    checked={}
    for x in range(len(nums)):
        diff=target-nums[x]
       
        if diff in checked:
            return [checked[diff],x] 
        else:
            checked[nums[x]]=x
    
