class Solution:
    def subarraySum(self, a: List[int], k: int) -> int:
        n = len(a)
        l = {0:1}
        s = 0
        maxlen = 0
        for i in range(n):
            s+=a[i]
            
            if s - k in l:
                maxlen +=l[s-k]
            if s not in l: l[s] = 1
            else:
                l[s]+=1
        return maxlen