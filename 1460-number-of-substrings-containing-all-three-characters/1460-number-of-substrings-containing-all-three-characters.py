class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = [-1,-1,-1]
        res = 0
        for i in range(len(s)):
            l[97 - ord(s[i])] = i
            
            
            res += 1+min(l)
        return res 
