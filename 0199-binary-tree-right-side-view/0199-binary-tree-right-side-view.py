# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)
        q = deque([[root,0]])
        if not root:
            return []
        while q:
            for i in range(len(q)):
                r,x = q.popleft()
                if r.left:
                    q.append([r.left,x+1])
                if r.right:
                    q.append([r.right,x+1])
                d[x] = r.val
        return [d[i] for i in sorted(d.keys())]