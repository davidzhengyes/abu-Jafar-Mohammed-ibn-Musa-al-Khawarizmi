#https://leetcode.com/problems/top-k-frequent-elements/
#method
#sort them?
#sorting will be nlogn
#beside that we can use n to count the ones with most occurrences
#mine prob not good.
#well had ok idea just didnt implement properly.


def topKFrequent(nums,k):
    count={}
    freq=[[] for i in range(len(nums)+1)]

    for n in nums:
        count[n]=1+count.get(n,0)
    for n,c in count.items():
        freq[c].append(n)
    
    res=[]
    for i in range(len(freq)-1,-1):
        for n in freq[i]:
            res.append(n)
        if len(res)==k:
            return res

# def topKFrequent(nums,k):
#     nums.sort()
#     #can use .insert for subbing elements.
#     topkvalue=[]
#     topkfrequency=[]  
#     for x in range(k):
#         topkvalue.append(0)
#         topkfrequency.append(0)
        
    
#     curr=nums[0]
#     currcount=0
#     for x in range(len(nums)):
#         if (not (curr==nums[x])) or x==len(nums)-1:
#             values=insert_freq(currcount,topkfrequency)
#             print(values,currcount,topkfrequency)
#             topkfrequency=values[2]
#             topkvalue.insert(values[1],curr)
#             topkvalue=topkvalue[0:len(topkvalue)-1]

#             curr=nums[x]
#             currcount=1
#         else:
#             currcount+=1

#     return topkvalue

# def insert_freq(n, freq):
#     for x in range(len(freq)):
#         if n>freq[x]:
#             freq.insert(x,n)
#             return [True,x,freq[0:len(freq)-1]]
#     return[False]
        
            
