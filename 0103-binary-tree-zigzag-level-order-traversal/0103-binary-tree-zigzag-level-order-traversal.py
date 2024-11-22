# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([root])
        c=0
        ans=[]
        if not root:
            return []
        while q:
            size = len(q)
            level = []
            c+=1
            for i in range(size):
                ele = q.popleft()
                level.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            if c%2 == 0:
                ans.append(level[::-1])
            else:
                ans.append(level)
        
        return ans
            
                