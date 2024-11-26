# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [[root,0,0]]
        d = {}
        while q:
            n = len(q)
            
            for i in range(n):
                r,x,y = q.pop(0)
                if r.left:
                    q.append([r.left,x+1,y-1])
                if r.right:
                    q.append([r.right,x+1,y+1])
                if y not in d:
                    d[y]=[]
                d[y].append([x,r.val])
        ans = []
        print(d)
        for i in sorted(d.keys()):
            x=[]
            for j in sorted(d[i]):
                x.append(j[1])
            ans.append(x)

        return ans