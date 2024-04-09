#Swim in Rising Water
import heapq
def swimInWater(grid):
    N = len(grid)
    visit = set()
    minH = [[grid[0][0], 0, 0]]
    print(minH)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visit.add((0, 0))
    while minH:
        time, r, c = heapq.heappop(minH)
        print(time, r, c)
        if r == N - 1 and c == N - 1:
            return time
        for dr, dc in directions:
            neiR, neiC = r + dr, c + dc
            print(neiR, neiC)
            if (neiR < 0 or neiC < 0 or neiR == N or neiC == N or (neiR, neiC) in visit):
                continue
            visit.add((neiR, neiC))
            heapq.heappush(minH, [max(time, grid[neiR][neiC]), neiR, neiC])
            print(visit)
            print(minH)
        print(minH)


#grid1 = [[0, 2], [1, 3]]
         
#grid2 = [[0, 1, 2, 3, 30], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
#grid3 = [[1,2,3], [4,5,6], [7,8,9]]
grid3 = [[1,2,3], [4,5,7], [6,2,4]]
#grid3 = [[1,9,2,4], [7,9,1,5], [8,8,1,4], [6,7,8,2]]
print(grid3)
#print(swimInWater(grid1))  
#print(swimInWater(grid2))  
print(swimInWater(grid3))
