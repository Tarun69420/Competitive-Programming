#506 Relative Ranks
import heapq
def findRelativeRanks(score):
    heap =[]
    for i, s in enumerate(score):
        heapq.heappush(heap,(-s,i))
    print(heap)
    ranks = [""] * len(score)
    print(ranks)
    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    for i in range(len(score)):
        s,index = heapq.heappop(heap)
        if i < 3:
            ranks[index] = medals[i]
        else:
            ranks[index] = str(i + 1)
    
    return ranks
    

# Test cases
print(findRelativeRanks([5,4,3,2,1]))  # Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
print(findRelativeRanks([10,3,8,9,4])) # Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
