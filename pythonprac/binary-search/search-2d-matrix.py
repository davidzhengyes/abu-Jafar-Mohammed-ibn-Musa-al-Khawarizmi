#https://leetcode.com/problems/search-a-2d-matrix/
#binary search to find array.
#binary search the inside lollllllllllll
#make sure to not go n*log(m) or something !!!

#but len(matrix) already makes it m(logN)??
#oh no len(matrix) is o(1).
def searchMatrix(matrix,target):
    if target<matrix[0][0]:
        return False
    if target>matrix[len(matrix)-1][len(matrix[len(matrix)-1])-1]:
        return False
    #both these are just if target is smaller than the smallest number or bigger than the biggest

    l=0
    r=len(matrix)-1

    if matrix[l][0]==target or matrix[r][0]==target:
        return True
    

    while (r-l)>1:
        
        middle=(l+r)//2
        print(l,middle,r)
        if matrix[middle][0]==target:
            return True
        elif matrix[middle][0]>target:
            r=middle
        else:
            l=middle

    #now binary search on matrix[l]
    if target>matrix[r][0]:
        newarr=matrix[r]
    else:
        newarr=matrix[l]
    print(newarr)
    l=0
    r=len(newarr)-1
    print(newarr)
    while l<=r:
        middle=(r+l)//2

        if newarr[middle]>target:
            r=middle-1
        elif newarr[middle]<target:
            l=middle+1
        else:
            return True
    return False

    
   