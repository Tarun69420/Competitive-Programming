class Solution:
    def subarraySum(self, a: List[int], k: int) -> int:
        n = len(a)
        l = {0:1}
        s = 0
        maxlen = 0
        for i in range(n):
            s+=a[i]
            
            
            maxlen +=l.get(s-k,0)
            l[s] = l.get(s,0)+1
        return maxlen