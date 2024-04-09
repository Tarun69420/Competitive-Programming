
#1464. Maximum Product of Two Elements in an Array
import heapq
def MaxPro2Ele(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
    print(heap)
    x = (-heapq.heappop(heap)-1)
    y = (-heapq.heappop(heap)-1)
    return x*y
    
nums = [3,4,5,2]
print(MaxPro2Ele(nums))
