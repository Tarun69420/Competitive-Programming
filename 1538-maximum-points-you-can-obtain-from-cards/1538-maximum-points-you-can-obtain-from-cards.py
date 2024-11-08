class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum=msum=rsum=0
        rindex = -1
        lsum = msum = sum(cardPoints[:k])
        for i in range(k-1,-1,-1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rindex]
            msum = max(lsum+rsum,msum)
            rindex-=1
        return msum
