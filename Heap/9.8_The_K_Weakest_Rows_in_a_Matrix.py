#1337. The K Weakest Rows in a Matrix
import heapq
def KWeakestRows(mat,k):
    heap=[]
    for i,v in enumerate(mat):
        heapq.heappush(heap,(sum(v),i))
    print(heap)
    result=[]
    for i in range(k):
        v , index = heapq.heappop(heap)
        result.append(index)
    print(result)
mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]] 
k = 3 
KWeakestRows(mat,k)
