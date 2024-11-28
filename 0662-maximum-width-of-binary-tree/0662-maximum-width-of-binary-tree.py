# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([[root,0]])
        maxwid = 0 
        while q:
            l,r = 0,0
            size = len(q)
            for i in range(size):
                x,ind = q.popleft()
                
                if ind != 0:
                    ind-=1
                    
                if i==0:
                    l=ind
                elif i==size-1:
                    r = ind
                if x.left:
                    q.append([x.left,2*ind+1])
                if x.right:
                    q.append([x.right,2*ind+2])
                
            maxwid = max(maxwid,-l+r+1)
        return maxwid
            
            
            