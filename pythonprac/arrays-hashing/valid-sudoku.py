#https://leetcode.com/problems/valid-sudoku/
#just check if repeated digits?


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
            print(threexthree)
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