class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n <0:
            sol = poww(x,-1*n)
            return 1/sol
        else:
            return poww(x,n)
def poww(x,n):
    if n == 1:
        return x
    if n%2 == 0:
        return poww(x*x,n//2)
    if n%2 == 1:
        return x*poww(x,n-1)




