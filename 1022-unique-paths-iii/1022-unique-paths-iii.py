class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ss = len(grid)
        sss = len(grid[0])
        gc=0
        for i in range(ss):
            for j in range(sss):
                if grid[i][j] == 1:
                    start = [i,j]
                elif grid[i][j] == 2:
                    end= [i,j]
                elif grid[i][j] == 0:
                    gc+=1
        def bs (grid,i,j,gc,visit):
            if (i,j) in visit or i>=ss or i<0 or j>=sss or j<0 or grid[i][j]==-1:
                return 0
            if i == (end[0]) and j == (end[1]):
                return 1 if gc == 0 else 0
            visit.add((i,j))
            a=bs(grid,i+1,j,gc-1,visit)
            b=bs(grid,i,j+1,gc-1,visit)
            c=bs(grid,i-1,j,gc-1,visit)
            d=bs(grid,i,j-1,gc-1,visit)
            visit.discard((i,j))
            return a+b+c+d
        return bs(grid,start[0],start[1],gc+1,set())