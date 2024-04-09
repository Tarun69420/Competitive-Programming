#703 kth largest element in a stream

import heapq

def kth_largest(k, nums,added):
    results = []
    heapq.heapify(nums)
    print(nums)
    for v in added:
        heapq.heappush(nums, v)
        print(nums)
        for i in range(len(nums)- k):
            heapq.heappop(nums)
        results.append(nums[0])
    print(results)

# Test case
k = 3
nums = [4, 5, 8, 2]
added = [3, 5, 10, 9, 4]
kth_largest(k, nums,added) 

'''
class KthLargest:

    def __init__(self, k: int, nums: List[int] ):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]   


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
'''
