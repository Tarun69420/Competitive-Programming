# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def checkheight(root):
            if not root:
                return 0
            l = checkheight(root.left)
            r = checkheight(root.right)
            return max(l,r)+1
        def dfs(root):
            if not root:
                return True
            
            l = checkheight(root.left)
            r = checkheight(root.right)
            print(l,r)
            if abs(l-r)>1:
                return False
            lc = dfs(root.left)
            rc = dfs(root.right)
            if not rc or not lc:
                return False
            return True
        return dfs(root)

        