class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(nums,s,e):
            while s<=e:
                nums[s],nums[e] = nums[e],nums[s]
                s+=1
                e-=1
        ind = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind = i
                #print(ind)
                break
        if ind ==-1:
            rev(nums,0,len(nums)-1)
            return
        for i in range(len(nums)-1,ind,-1):
            if nums[ind] < nums[i]:
                nums[i],nums[ind] = nums[ind],nums[i]
                break
        
        rev(nums,ind+1,len(nums)-1)
        