class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = -1
        cnt = 0
        for i in range(len(nums)):
            if cnt  == 0:
                maj = nums[i]
                cnt+=1
            elif nums[i]==maj:
                cnt+=1
            elif nums[i]!= maj:
                cnt-=1
        return maj