class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = r = 0
        s= 0
        maxsum = 0
        d = defaultdict(int)
        while r<len(nums):
            d[nums[r]]+=1
            s+=nums[r]
            while d[nums[r]]>1:
                d[nums[l]]-=1
                s-=nums[l]
                l+=1
            maxsum = max(maxsum,s)
            r+=1
        return maxsum
