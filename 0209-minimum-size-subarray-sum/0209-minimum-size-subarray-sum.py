class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=r=0
        s = 0
        minlen = 10**9
        while r<len(nums):
            s+=nums[r]
            while s >= target:
                minlen = min(r-l+1,minlen)
                s-=nums[l]
                l+=1
            r+=1
        return 0 if minlen == 10**9 else minlen