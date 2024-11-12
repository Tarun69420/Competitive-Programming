class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = r = 0
        s=""
        while l<len(word1) and r<len(word2):
            s+=word1[l]+word2[r]
            l+=1
            r+=1
        s+=word1[l:]
        s+=word2[r:]
        return s