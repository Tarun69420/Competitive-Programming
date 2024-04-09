#Car Pooling
import heapq

def carPooling(trips, capacity):
    heap = []
    for numPassengers, start, end in trips:
        heap.extend([(start, numPassengers), (end, -numPassengers)])
        print(heap)
    heapq.heapify(heap)
    print(heap)
        
    while capacity >= 0 and heap:
        capacity -= heapq.heappop(heap)[1]
        print(heap)
        print(capacity)
    return len(heap) == 0

#trips = [[2,1,5],[3,3,7]]
#capacity = 4 
trips = [[4,1,5],[1,2,4],[1,4,5]]
capacity = 5
print(trips, capacity)
print(carPooling(trips, capacity))  

