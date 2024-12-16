class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        summ = 0
        for i in nums:
            summ+=i
            if summ<0:
                summ=0
            elif summ>maxi:
                maxi = summ
        return maxi if maxi != (float("-inf")) else max(nums)