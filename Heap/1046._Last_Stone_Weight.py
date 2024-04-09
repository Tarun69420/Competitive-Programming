#1046. Last Stone Weight
import heapq
def LastStoneWeight(stones):
    heap = []
    for num in stones:
        heapq.heappush(heap, -num)
        print(heap)
    
    print(heap)
    while len(heap) > 1:
        x = -heapq.heappop(heap)
        print(x)
        y = -heapq.heappop(heap)
        print(y)
        if x == y:
            continue
        else:
            heapq.heappush(heap, -(x - y))
        print(heap)
        
    return 0 if not heap else -heap[0]

stones = [2,7,4,1,8,1]
print(stones)
#stones = [2, 2]
print(LastStoneWeight(stones))  

