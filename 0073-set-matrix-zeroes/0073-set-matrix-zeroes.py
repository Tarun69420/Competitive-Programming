class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0=1
        r,c=len(m),len(m[0])
        for i in range(r):
            for j in range(c):
                if m[i][j]==0:
                    if j==0:
                        col0=0
                        m[i][0]=0
                    else:
                        m[i][0]=0
                        m[0][j]=0
        print(col0)
        for i in range(1,r):
            for j in range(1,c):
                
                #print(m[i][0],m[0][j])
                if  m[i][j]!=0:
                    if m[i][0]==0 or m[0][j] == 0:
                        m[i][j] = 0

        if m[0][0] == 0:
            m[0]=[0]*c
        
        if col0 == 0:
            for i in range(r):
                m[i][0] = 0
        
        
        
       
            