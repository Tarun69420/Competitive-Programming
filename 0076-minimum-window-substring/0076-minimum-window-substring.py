class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = c = 0
        n = len(s)
        m = len(t)
        start = -1
        d = Counter(t)
        minlen = 10**9
        while r<len(s):
            if s[r] in d and d[s[r]] > 0:
                c+=1
            elif s[r] not in d:
                d[s[r]]=-1
            d[s[r]]-=1
            while c == m:
                if (r-l+1 < minlen):
                    minlen = r-l+1
                    start = l
                d[s[l]]+=1
                if d[s[l]] > 0:
                    c-=1
                l+=1
            r+=1
        return "" if start == -1 else s[start:start+minlen]