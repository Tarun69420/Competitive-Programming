class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        self.bs(nums,0,ans,[])
        return ans
    def bs(self,nums,i,ans,ds):
        if ds:
                ans.append(ds[:])
        if i >= len(nums):
                return
        for j in range(i,len(nums)):
            if j != i and nums[j] == nums[j-1]:
                continue
            ds.append(nums[j])
            self.bs(nums,j+1,ans,ds)
            ds.pop()
        

