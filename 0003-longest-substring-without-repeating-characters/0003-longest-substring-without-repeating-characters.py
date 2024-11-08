class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        for i in set(s):
            d[i] = 0
        l=0
        r=0
        mlen = 0
        while (r<len(s)):
            if  d[s[r]] == 0:
                d[s[r]] = 1
                r+=1
            else:
                d[s[l]] -= 1
                l+=1
            mlen = max(r-l,mlen)
        return mlen