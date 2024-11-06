class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.bs(s,[],ans,0)
        return ans
    def bs (self,s,ds,ans,i):
        if i == len(s):
            ans.append(ds[:])
            return
        for j in range(i+1,len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                ds.append(s[i:j])
                self.bs (s,ds,ans,j)
                ds.pop()
        return
