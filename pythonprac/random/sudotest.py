def findempty(board):
    foundempty=False
    boardX=0
    boardY=0
    for x in range(9):
        for y in range(9):
     
            if board[x][y]==".":
                boardX=x
                boardY=y
                foundempty=True
                break
        if foundempty:
            break  
    print(boardX,boardY)

findempty([['5', '3', '9', '9', '7', '9', '9', '9', '.'], 
           ['6', '.', '.', '1', '9', '5', '.', '.', '.'], 
           ['.', '9', '8', '.', '.', '.', '.', '6', '.'], 
           ['8', '.', '.', '.', '6', '.', '.', '.', '3'], 
           ['4', '.', '.', '8', '.', '3', '.', '.', '1'], 
           ['7', '.', '.', '.', '2', '.', '.', '.', '6'], 
           ['.', '6', '.', '.', '.', '.', '2', '8', '.'], 
           ['.', '.', '.', '4', '1', '9', '.', '.', '5'], 
           ['.', '.', '.', '.', '8', '.', '.', '7', '9']])


# a=5

# def changeNumber(var):
#     var=6

# changeNumber(a)
# print(a)


# a=[1,2,3]
# b=a.copy()
# print(b)
# b[0]=4
# print(b)
# print(a)

def isValidSudoku(board):
    #rows
    for x in range(9):
        if not isValidArray(board[x]):
            return False
    #columns
    for x in range(9):
        column=[]
        for y in range(9):
            column.append(board[y][x])
        if not isValidArray(column):
            return False
    
    for x in range(3):
        for y in range(3):
            threexthree=[]
            threexthree+=board[x*3][y*3:y*3+3]
            threexthree+=board[x*3+1][y*3:y*3+3]
            threexthree+=board[x*3+2][y*3:y*3+3]
            if not isValidArray(threexthree):
                return False
    return True

def isValidArray(nine):
    visited=set()
    for x in nine:
        if not x==".":
            if x in visited:
                return False
            visited.add(x)
    return True

# b=[['5', '3', '1', '2', '7', '4', '8', '9', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
# for x in range(1,10):
#     b[0][8]=str(x)
#     print(isValidSudoku(b))

# print("\n")

if "Abc":
    print("hi")
