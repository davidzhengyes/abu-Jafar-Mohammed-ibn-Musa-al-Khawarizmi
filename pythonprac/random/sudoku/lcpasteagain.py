class Solution:
    board=[]
    def solveSudoku_rec(self,bo):
        global board
        # print(b)
        #dont actually modify the real board.
        #maybe this is inefficient with memory
        #prob don't need this as it is local scope.
        # currentBoard=board.copy()
        currentBoard=self.myCopy(bo)
        # if m:
        #     print(currentBoard)
        
        
        foundempty=False
        # boardX=0
        # boardY=0
        for x in range(9):
            for y in range(9):
        
                if bo[x][y]==".":
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
            bo=self.myCopy(currentBoard)
            if foundempty:
                
                bo[boardX][boardY]=str(x)
                # if m:
                #     print(currentBoard)
                #     print(board)
                #     print("\n")

                if self.isValidSudoku(bo):
                
                    if self.solveSudoku_rec(bo)==True:
                        self.board[boardX][boardY]=str(x)
                        # print(b)
                        # print("returned true2 here")
                        return True
            else:
                if foundempty==False and self.isValidSudoku(bo):
                

                    # b[8][8]=str(x)
                    # print(b)
                    # print("returned true1 here")
                    return True
        #means from 1,9, did not find a solution
        #aaaa should not return False bc that breaks the program immediately
                #return something that isn't true
        #hmm it's going all the way through
                
        return "a"

    def isValidSudoku(self,board):
        #rows
        for x in range(9):
            if not self.isValidArray(board[x]):
                return False
        #columns
        for x in range(9):
            column=[]
            for y in range(9):
                column.append(board[y][x])
            if not self.isValidArray(column):
                return False
        
        for x in range(3):
            for y in range(3):
                threexthree=[]
                threexthree+=board[x*3][y*3:y*3+3]
                threexthree+=board[x*3+1][y*3:y*3+3]
                threexthree+=board[x*3+2][y*3:y*3+3]
                if not self.isValidArray(threexthree):
                    return False
        return True

    def isValidArray(self,nine):
        visited=set()
        for x in nine:
            if not x==".":
                if x in visited:
                    return False
                visited.add(x)
        return True

    def myCopy(self,arr):
        res=[]
        for x in range(9):
            row=[]
            for y in range(9):
                row.append(arr[x][y])
            res.append(row)
        return res
    def solveSudoku(self, board) -> None:
        self.board=board
        self.solveSudoku_rec(board)
        """
        Do not return anything, modify board in-place instead.
        """


a=Solution()
board = [[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]]
a.solveSudoku(board)
print(board)