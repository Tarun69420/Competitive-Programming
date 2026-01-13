class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        mem = [[-1]*n for i in range(m)]
        #return self.calpath(grid,m-1,n-1,mem)
        return self.tab_CP(grid)
    def calpath(self,grid,row,col,mem):
        if row == 0 and col == 0 :
            return grid[row][col]
        if row <0 or col <0:
            return float("inf")
        if mem[row][col] != -1:
            return mem[row][col]
        left = grid[row][col]+self.calpath(grid,row-1,col,mem)
        right = grid[row][col]+self.calpath(grid,row,col-1,mem)

        mem[row][col]=min(left,right)
        return mem[row][col]
    def tab_CP(self,grid):
        m,n = len(grid),len(grid[0])
        mem = [[-1]*n for i in range(m)]

        

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    mem[0][0] = grid[0][0]
                else:
                    left,right = float("inf"),float("inf")
                    if i>0:
                        left = grid[i][j] + mem[i-1][j]
                    if j>0:
                        right = grid[i][j] + mem[i][j-1]
                    mem[i][j] = min(left,right)
        return mem[m-1][n-1]
            

