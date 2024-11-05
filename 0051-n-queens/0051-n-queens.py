class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."]*n for i in range(n)]
        self.solve(0,n,board,ans)
        return ans
    def solve(self,col,n,board,ans):
        if col == n:
            x = ["".join(i) for i in board]
            ans.append(x)
            print(board)
            return
        for i in range(0,n):
            if self.safe(i,col,n,board):
                board[i][col] = "Q"
                self.solve(col+1,n,board,ans)
                board[i][col] = "."
        return
    def safe(self,row,col,n,board):
        r = row
        c = col
        while r >=0 and c >=0:
            if board[r][c] == "Q":
                return False
            r-=1
            c-=1
        r = row
        c = col
        while c>=0:
            if board[r][c] =="Q":
                return False
            c-=1
        r = row
        c = col

        while r<n and c>=0:
            if board[r][c] == "Q":
                return False
            c-=1
            r+=1
        return True

        
