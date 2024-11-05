class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.bs(n,k,[],ans,1)
        return ans
    def bs (self,n,k,ds,ans,i):
        if k == 0:
            ans.append(ds[:])
            return
        if i>n:
            return
        for j in range(i,n+1):
            ds.append(j)
            self.bs(n,k-1,ds,ans,j+1)
            ds.pop()
        return