from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use a defaultdict to store nodes at each vertical and horizontal level.
        nodes = defaultdict(list)
        q = [(0, 0, root)]  # (horizontal distance, vertical level, node)

        while q:
            hd, level, node = q.pop(0)

            # Store the node in the dictionary. We use a heap to sort by level and value.
            heappush(nodes[hd], (level, node.val))

            if node.left:
                q.append((hd - 1, level + 1, node.left))
            if node.right:
                q.append((hd + 1, level + 1, node.right))

        # Extract the results from the dictionary
        ans = []
        for hd in sorted(nodes.keys()):  # Process horizontal distances in sorted order
            col = []
            while nodes[hd]:
                _, val = heappop(nodes[hd])  # Extract nodes sorted by level and value
                col.append(val)
            ans.append(col)

        return ans
