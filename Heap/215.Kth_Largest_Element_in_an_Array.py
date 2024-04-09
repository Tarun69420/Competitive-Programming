#Kth Largest Element in an Array
'''
import heapq
def findKthLargest(nums, k):
    print(nums)
    min_heap = []
    #min_heap=nums[:k]
    for num in nums[:k]:
        heapq.heappush(min_heap, num)
    print(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            print(min_heap)
            heapq.heappush(min_heap, num)
            print(min_heap)
    return min_heap[0]

print(findKthLargest([3,2,1,5,6,4], 2))  
#print(findKthLargest([3,2,3,1,2,4,5,5,6], 5))

'''

import heapq

def findKthLargest(nums, k):
    heapq.heapify(nums)
    r=len(nums)-k
    #if r>0:
      #  return heapq.heappop(nums)
    for i in range (r):
        
        heapq.heappop(nums)
        print(nums)
    return nums[0]


nums1 = [3, 2, 1, 1,5, 6, 4]
k1 = 2
print(findKthLargest(nums1, k1))  # Output: 5

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(findKthLargest(nums2, k2))  # Output: 4

'''
import heapq

def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
        print(heap)
    for i in range(k - 1):
        heapq.heappop(heap)
    print(heap)
    return -heapq.heappop(heap)


nums1 = [3, 2, 1, 1,5, 6, 4]
k1 = 2
print(findKthLargest(nums1, k1))  # Output: 5

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(findKthLargest(nums2, k2))  # Output: 4
'''

