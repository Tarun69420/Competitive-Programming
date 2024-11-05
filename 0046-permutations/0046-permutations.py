class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        d = {i:0 for i in nums}
        ans=[]
        self.bs(nums,0,[],ans,d)
        return ans
    def bs(self,nums,i,ds,ans,d):
        if i == len(nums):
            ans.append(ds[:])
            return
        for j in d:
            if d[j] == 0:
                d[j]=1
                ds.append(j)
                self.bs(nums,i+1,ds,ans,d)
                ds.pop()
                d[j]=0
        return