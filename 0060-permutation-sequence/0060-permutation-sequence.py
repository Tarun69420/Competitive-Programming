class Solution:
    
    def getPermutation(self, n: int, k: int) -> str:
        d = [str(i) for i in range(1,n+1)]
        return self.bs(n,k-1,d,"")
        
    def bs (self,n,k,d,ds):
        if len(d) == 0:
            return ds
        nn  = self.fact(n-1)
        ds+=d.pop(k//nn)
        return self.bs(n-1,k%nn,d,ds)
         

    def fact(self,a):
        if a<=0:
            return 1
        return a*self.fact(a-1)