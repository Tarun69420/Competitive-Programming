# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        d=0
        if not root:
            return d
        while q:
            size = len(q)
            
            d+=1
            for i in range(size):
                ele=q.popleft()
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
        return d
