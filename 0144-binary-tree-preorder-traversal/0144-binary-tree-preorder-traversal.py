# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preord = []
        cur = root
        while cur:
            if not cur.left:
                preord.append(cur.val)
                cur=cur.right
            else:
                pre=cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    preord.append(cur.val)
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right
        return preord