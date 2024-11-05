class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        self.bs(nums,0,ans,[])
        return ans
    def bs (self,nums,i,ans,ds):
        if i == len(nums):
            if ds:
                ans.append(ds[:])
                return
        
            return
        ds.append(nums[i])
        self.bs(nums,i+1,ans,ds)
        ds.pop()
        self.bs(nums,i+1,ans,ds)
        return