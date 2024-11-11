class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.helper(nums,k)-self.helper(nums,k-1)
    def helper(self,nums,k):
        l = r = c = 0
        d={}
        if k <= 0:
            return 0
        while r<len(nums):
            if nums[r] not in d:
                d[nums[r]] = 1
            else:
                d[nums[r]]+=1
            while len(d)>k:
                d[nums[l]]-=1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l+=1
            c+=r-l+1
            r+=1
        return c