class Solution:
    def numSubarraysWithSum(self, nums: List[int], goals: int) -> int:
        return self.helper(nums,goals)-self.helper(nums,goals-1)
    def helper(self,nums,k):
        l = r = c = 0
        s=0
        if k<0: return 0
        while r<len(nums):
            s+=nums[r]
            while s>k:
                s-=nums[l]
                l+=1
            c+=(r-l+1)
            r+=1
        return c