class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.bs(candidates,0,target,[],ans)
        return ans
    def bs (self,candidates,i,target,ds,ans):
        if target == 0:
            ans.append(ds[:])
            return
        for j in range(i,len(candidates)):
            if j>i and candidates[j]==candidates[j-1]:
                continue
            if candidates[j] > target:
                break
            ds.append(candidates[j])
            self.bs(candidates,j+1,target-candidates[j],ds,ans)
            ds.pop()