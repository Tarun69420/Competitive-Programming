class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.bs(n,k,1,ans,[])
        return ans
    def bs(self,target,n,i,ans,ds):
        if n == 0 and target == 0:
            ans.append(ds[:])
            return
        for j in range(i,10):
            if j > target:
                break
            ds.append(j)
            self.bs(target-j,n-1,j+1,ans,ds)
            ds.pop()
        return 