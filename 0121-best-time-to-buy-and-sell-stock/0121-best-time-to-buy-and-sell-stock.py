class Solution:
    def maxProfit(self, l: List[int]) -> int:
        minele = l[0]
        profit = 0
        cost = 0
        for i in range(1,len(l)):
            profit = max(l[i]-minele,profit)
            minele = min(minele,l[i])
        return profit
    
        