




def insertionSort(unsortlist):
    if len(unsortlist)==2:
        return (insert (unsortlist[0],[unsortlist[1]]))

    
    sortedlist=insert(unsortlist[0],insertionSort(unsortlist[1:len(unsortlist)]))
    return sortedlist
        
        
    


def insert (n, sortedlist):
    x=0
    while x<len(sortedlist):
        if sortedlist[x]>=n:
            sortedlist.insert(x,n)
            break
        x+=1

    if x==(len(sortedlist)):
        sortedlist.append(n)

    return sortedlist
