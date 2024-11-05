class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        d = {i:0 for i in nums}
        ans=[]
        self.bs(nums,0,[],ans,d)
        return ans
    def bs(self,nums,i,ds,ans,d):
        if i == len(nums):
            ans.append(nums[:])
            return
        for j in range(i,len(nums)):
            nums[j],nums[i] = nums[i],nums[j]
            self.bs(nums,i+1,ds,ans,d)
            nums[j],nums[i] = nums[i],nums[j]
            
        return