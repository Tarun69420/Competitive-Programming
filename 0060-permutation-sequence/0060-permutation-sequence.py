class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        d = [str(i) for i in range(1, n + 1)]  # Initialize with all numbers in string format
        fact = 1
        for i in range(1, n):
            fact *= i

        return self.bs(n, k - 1, d, "", fact)
    
    def bs(self, n, k, d, ds, fact):
        if not d:
            return ds
        
        index = k // fact
        ds += d.pop(index)
        k %= fact
        if n > 1:
            fact //= (n - 1)  # Reduce factorial for the next recursive call
            
        return self.bs(n - 1, k, d, ds, fact)
