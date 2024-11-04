class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.bs(candidates,target,[],ans,0,len(candidates))
        return ans
    def bs(self,candidates,target,ds,ans,i,n):
        if target == 0:
            ans.append(ds[:])
            print(ds)
            return
        elif target <0:
            return
        for j in range(i,n):
                ds.append(candidates[j])
                self.bs(candidates,target-candidates[j],ds,ans,j,n)       
                ds.pop()

               
                    

            
