# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = -100000000000
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.dfs(root)
        return self.sum
    def dfs(self,root):
            if not root:
                return 0
            
            l = max(0,self.dfs(root.left))
            r = max(0,self.dfs(root.right))
            self.sum = max(self.sum,l+r+root.val)
            return max(l,r)+root.val
