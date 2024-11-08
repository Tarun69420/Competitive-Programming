class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.bs(n*2,"",ans)
        return ans
    def bs(self,n,s,ans):
        if  n == 0:
            if self.valid(s):
                ans.append(s)
            return
            
        self.bs (n-1,s+"(",ans)
        self.bs (n-1,s+")",ans)
        return
    def valid(self,s):
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False