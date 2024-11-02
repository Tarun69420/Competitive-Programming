class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return dp(grid,len(grid)-1,len(grid[0])-1,{})
def dp(grid,i,j,temp):
 
 
        if i<0 or j<0:
            return float('inf')
        
        if i == 0 and j == 0:
            return grid[0][0]
        if (i,j) in temp:
            return temp[(i,j)]
        
        s = dp(grid,i-1,j,temp)
        w = dp(grid,i,j-1,temp)
        temp[(i,j)]= min(s,w)+grid[i][j]
        return temp[(i,j)]