#https://leetcode.com/problems/contains-duplicate/
#was initially thinking to sort, but mergesort? too much recursion for python i guess
#insertion sort takes the same time?
#wait can u use built in sort fn
# def containsDuplicate (lon):
#     duplicate=False
#     lon.sort()
#     for x in range(len(lon)-1):
#         if lon[x]==lon[x+1]:
#             duplicate=True
#             break
#     return duplicate

def containsDuplicate(lon):
    visited=set()
    for x in lon:
        if x in visited:
            return True
        visited.add(x)
        
    return False
        

