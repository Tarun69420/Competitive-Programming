class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        z = 0
        mlen = 0
        while r < len(nums):
            if nums[r] == 0:
                z+=1   
            if z>k:
                if nums[l] == 0:
                    z-=1
                l+=1
            if z<=k:
                mlen = max(r - l + 1 , mlen)
            r+=1
        return mlen
