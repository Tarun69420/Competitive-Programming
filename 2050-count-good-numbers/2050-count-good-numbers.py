class Solution:
    
    def countGoodNumbers(self, n: int) -> int:
        y = n//2
        mod = 10**9+7
        if n == 1:
            return 5
        if n%2 == 0:
            return self.pow(20,y)%(mod)
        return (self.pow(20,y)*5)%(mod)
    def pow (self,x,n):
        
        if n == 0:
            return 1
        if n%2 == 0:
            return self.pow((x*x)%(10**9+7),n//2)
        else:
            return (x*self.pow(x,n-1))%(10**9+7)
