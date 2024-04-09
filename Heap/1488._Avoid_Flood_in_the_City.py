def avoidFlood(self, rains: List[int]) -> List[int]:
	from collections import defaultdict
	import heapq

	# The first step is to save the list of lake indexes to a hash table.
	# e.g., cache = { lake id: [list of indices]}
	cache = defaultdict(list)
	for i in range(len(rains)):
		cache[rains[i]].append(i)

	full = set()
	heap = []
	ans = []

	for i in range(len(rains)):
		if rains[i] == 0:
			if heap:
				# Index of the lake where the rain comes next
				next_index = heapq.heappop(heap)
				if rains[next_index] in full:
					ans.append(rains[next_index])
					full.remove(rains[next_index])
			else:
				ans.append(1)
		else:
			if rains[i] in full:
				return []
			else:
				full.add(rains[i])
				cache[rains[i]].pop(0)

				# If it still rains in the future, push the index to the heap
				if cache[rains[i]]:
					heapq.heappush(heap, cache[rains[i]][0])

				ans.append(-1)

	return ans
