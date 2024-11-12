class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = r = 0
        s = 0
        maxsum = 0
        d = set()
        
        while r < len(nums):
            # Check if nums[r] is already in the set
            while nums[r] in d:
                # Remove nums[l] from set and subtract from sum to adjust window
                d.discard(nums[l])
                s -= nums[l]
                l += 1
            
            # Now we can safely add nums[r] to the set
            d.add(nums[r])
            s += nums[r]
            # Update maxsum to the highest sum of unique subarrays so far
            maxsum = max(maxsum, s)
            r += 1
            
        return maxsum
