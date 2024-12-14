class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        '''
        temp = nums[n-k:]
        for i in range(n-k-1,-1,-1):
            #print(i)
            nums[(i+k)] = nums[i]
        for i in range(k):
            nums[i] = temp[i]
        '''
        def rev(l,s,e):
            while s<e:
                l[s],l[e]=l[e],l[s]
                s+=1
                e-=1
        
        rev(nums,0,n-1)
        rev(nums,0,k-1)
        rev(nums,k,n-1)
