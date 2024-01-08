#https://leetcode.com/problems/sudoku-solver/
#OH BOY OH BOY OH BOY RECURSION
#dont need an array for checking whih ones have a soln. if a soln is found, just put current num
# (1-9) in the cell. Check if you are in the cell ([8][8]) and if you have valid sudoku grid, then 
# return some kind of true, and that true indicates to fill in the correct cell with (1-9).
import time

def solveSudoku(board,m):
    global b
    # print(b)
    #dont actually modify the real board.
    #maybe this is inefficient with memory
    #prob don't need this as it is local scope.
    # currentBoard=board.copy()
    currentBoard=myCopy(board)
    if m:
        print(currentBoard)
      
    
    foundempty=False
    # boardX=0
    # boardY=0
    for x in range(9):
        for y in range(9):
     
            if board[x][y]==".":
                boardX=x
                boardY=y
                foundempty=True
                break
        if foundempty:
            break  
    # print(boardX,boardY)
    #if foundempty==false, we are on the last square in the grid, if we find a number 1-9 that isvalidsudoku,
    #we have solved it, return true 
    for x in range(1,10):
        # board=currentBoard.copy()
        board=myCopy(currentBoard)
        if foundempty:
            
            board[boardX][boardY]=str(x)
            # if m:
            #     print(currentBoard)
            #     print(board)
            #     print("\n")

            if isValidSudoku(board):
            
                if solveSudoku(board,False)==True:
                    b[boardX][boardY]=str(x)
                    # print(b)
                    # print("returned true2 here")
                    return True
        else:
            if foundempty==False and isValidSudoku(board):
               

                # b[8][8]=str(x)
                # print(b)
                # print("returned true1 here")
                return True
    #means from 1,9, did not find a solution
    #aaaa should not return False bc that breaks the program immediately
            #return something that isn't true
    #hmm it's going all the way through
            
    return "a"



 

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

b= [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

def myCopy(arr):
    res=[]
    for x in range(9):
        row=[]
        for y in range(9):
            row.append(arr[x][y])
        res.append(row)
    return res


a=b.copy()
print(solveSudoku (a,True))

print(b)