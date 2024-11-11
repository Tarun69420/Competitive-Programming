class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d=[0]*26
        l=r=mlen=0
        mfre=0
        while r <len(s):
            d[ord(s[r])-ord('A')]+=1
            mfre = max(mfre,d[ord(s[r])-ord('A')])
            if -mfre + (r-l+1) > k:
                d[ord(s[l])-ord('A')]-=1
                l+=1
            r+=1
        return len(s) - l