class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        mem = [[-1]*n for i in range(m)]
        return self.calpath(grid,m-1,n-1,mem)
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
