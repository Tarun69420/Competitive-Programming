# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', r1: 'TreeNode', r2: 'TreeNode') -> 'TreeNode':
       
        def dfs(root,r1,r2):
            if root == r1 or root == r2 or root == None:
                return root
            
            l =dfs(root.left,r1,r2)
            r=dfs(root.right,r1,r2)
            if l and r:
                return root
            return l if l else r
        
        return dfs(root,r1,r2)
        