# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inord = []
        cur = root
        if not root:
            return []
        while cur:
            if not cur.left:
                inord.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right!=cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                
                else:
                    inord.append(cur.val)
                    prev.right = None
                    cur = cur.right
        return inord