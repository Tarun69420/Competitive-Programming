from collections import defaultdict

class Solution:
    def subarraySum(self, a: List[int], k: int) -> int:
        n = len(a)
        l = defaultdict(int)
        l[0] = 1  # Initialize with sum 0 to handle cases where subarray starts from index 0
        s = 0
        count = 0
        
        for i in range(n):
            s += a[i]
            
            # Check if there's a previous sum that would result in a subarray sum of k

            count += l[s - k]
                
            # Increment the count of the current cumulative sum in the dictionary
            l[s] += 1
            
        return count
