# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root,ans):
            if not root:
                return 0
            l  = dfs(root.left,ans)
            r = dfs(root.right,ans)
            if ans[0]<l+r:
                ans[0] = l+r
            return max(l,r)+1
        ans = [0]
        dfs(root,ans)
        return ans[0]