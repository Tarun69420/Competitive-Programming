class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        arr=[1,2,3,4,5,6,7,8,9]
        self.bs(arr,n,k,1,ans,[])
        return ans
    def bs(self,arr,target,n,i,ans,ds):
        if n<0:
            return
        if len(ds) == n and target == 0:
            ans.append(ds[:])
            return
        for j in range(i,10):
            if j > target:
                break
            if target>=0:
                ds.append(j)
                self.bs(arr,target-j,n,j+1,ans,ds)
                ds.pop()
        return 