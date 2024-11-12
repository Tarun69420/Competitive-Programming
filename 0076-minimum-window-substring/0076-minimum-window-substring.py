class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict

        l = r = c = 0
        n = len(s)
        m = len(t)
        start = -1
        d = defaultdict(int)
        minlen = float('inf')
        
        # Fill in initial character counts of `t` in `d`
        for char in t:
            d[char] += 1
        
        while r < len(s):
            if d[s[r]] > 0:
                c += 1
            
            if s[r] in d:
                d[s[r]] -= 1
            
            while c == m:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    start = l

            
                d[s[l]] += 1
                if d[s[l]] > 0:
                        c -= 1
                l += 1
            
            r += 1
        
        return "" if start == -1 else s[start:start + minlen]
