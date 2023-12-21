#https://leetcode.com/problems/daily-temperatures/
#might go backwards into the stack, take the last element of list and drop it into the stack.
#reverse stack not work.


def dailyTemperatures(temperatures):
    res=[0]*len(temperatures)
    stack=[] #pair, temp, index

    stack.append([temperatures[0],0])
    for x in range(1,len(temperatures)):
  
        while stack and temperatures[x]>stack[-1][0]:
            t,ind=stack.pop()
            res[ind]=x-ind
            
        stack.append([temperatures[x],x])
   
    return res





# a=[0,1,2,3,4,5,6,7,8,9]

# for x in range(len(a)-1,-1,-1):
#     print(a[x])


# def dailyTemperatures(temperatures):
#     stack=[]
#     stack.append(0)

#     for x in range(len(temperatures)-2,-1,-1):
#         if temperatures[x]>temperatures[x+1]:



        
