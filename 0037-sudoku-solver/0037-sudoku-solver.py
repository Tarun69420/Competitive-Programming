class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.bs (board,0)
    def bs (self,board,row):
        if row == 9:
            return True
        for col in range(0,9):
            if board[row][col] == ".":
                for num in range(1,10):
                    if self.valid(board,row,col,str(num)):
                        board[row][col] = str(num)
                        if (self.bs(board,row)) == True:
                            return True
                        else:
                            board[row][col] = "."
                return False
        return self.bs(board,row+1)
        
        
    def valid (self,board,row,col,num):
        for i in range(9):
            if num == board[i][col]:
                return False
        for i in range(9):
            if num == board[row][i]:
                return False
        x,y = row - row % 3 , col - col % 3
        for i in range(x,x+3):
            for j in range(y,y+3):
                if board[i][j] == num:
                    return False
        return True