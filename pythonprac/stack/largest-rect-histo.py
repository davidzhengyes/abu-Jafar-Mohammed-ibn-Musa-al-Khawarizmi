#https://leetcode.com/problems/largest-rectangle-in-histogram/
#every time there is a bar of height 0 treat as a separate subproblem. 
#deal with each one like example 1


def largestRectangleArea(heights):
    maxArea=0
    stack=[]

    for i,h in enumerate(heights):
        start=i
        while stack and stack[-1][1]>h:
            index,height=stack.pop()
            maxArea=max(maxArea,height*(i-index))
            start=index
        stack.append((start,h))
    for i,h in stack:
        maxArea=max(maxArea,h*(len(heights)-i))
    return maxArea  


# def largestRectangle(heights):

#     stack=[]
#     height=heights[0]
    
#     stack.append([height,0])

#     maxarea=heights[0]
#     heights.append(0)

#     for x in range(1,len(heights)):
#         print(stack)
#         if not stack:
#             stack.append([heights[x],x])

#         elif stack and heights[x]>=stack[-1][0]:
#             stack.append([heights[x],x])
        
#         else:
#             while stack and heights[x]<stack[-1][0]:
#                 height,index=stack.pop()
#                 maxarea=max(maxarea,height*(x-index))
#                 print(x,index,maxarea)
# #need to push index all the way back, largestRectangle([2,1,2])
#     return maxarea