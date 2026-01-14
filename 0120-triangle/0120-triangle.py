class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m,n = len(triangle),len(triangle[-1])
        #return self.calsum(triangle,m-1,n-1,n)
        res= float("inf")
        for i in range(n):
            mem=[[-1]*(i+1) for i in range(m) ]
            res=min(res,self.calsum(triangle,m-1,i,mem))
        return res
        
    def calsum(self,triangle,i,j,mem):
        if i == 0 and j == 0:
            return triangle[i][j]
        if i<0 or j<0 or j>i:
            return float("inf")
        if mem[i][j]!=-1:
            return mem[i][j]
        left = triangle[i][j]+self.calsum(triangle,i-1,j,mem)
        right = triangle[i][j]+self.calsum(triangle,i-1,j-1,mem)

        mem[i][j]= min(left,right)
        return mem[i][j]