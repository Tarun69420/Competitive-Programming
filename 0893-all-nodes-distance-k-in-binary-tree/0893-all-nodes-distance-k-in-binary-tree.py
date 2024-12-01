# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        if k == 0:
            return [target.val]
        q = deque([root])
        ans = []
        parent = {}
        while q:
            for i in range(len(q)):
                x = q.popleft()
                if x.left:
                    q.append(x.left)
                    parent[x.left]=x
                if x.right:
                    q.append(x.right)
                    parent[x.right]=x
        q = deque([target])
        h = 0
        visited  = set()
        visited.add(target)
        while q:
            if h == k:
                return [n.val for n in q]
            
            for j in range(len(q)):
                x = q.popleft()
                
                if x.left and x.left not in visited:
                    visited.add(x.left)
                    q.append(x.left)
                if x.right and x.right not in visited:
                    visited.add(x.right)
                    q.append(x.right)
                if x in parent and parent[x] not in visited :
                    visited.add(parent[x])
                    q.append(parent[x])
            h+=1
        return []               
                
            
                