class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."]*n for i in range(n)]
        c = 0
        return self.solve(board,n,0)
        #return c
    def solve(self,board,n,col):
        if col == n: 
            return 1
        c = 0
        for row in range(n):
            if self.safe(board,row,col):
                board[row][col] = "Q"
                c += self.solve(board,n,col+1)
                board[row][col] = "."
        return c
        
    def safe(self,board,row,col):
        r = row
        c = col
        while (r>=0 and c>=0):
            if board[r][c] == "Q":
                return False
            r-=1
            c-=1
        c = col
        r = row
        while (c>=0):
            if board[r][c]=="Q":
                return False
            c-=1
        c = col
        while (r < len(board) and c>=0):
            if board[r][c] =="Q":
                return False
            r+=1
            c-=1
        return True

