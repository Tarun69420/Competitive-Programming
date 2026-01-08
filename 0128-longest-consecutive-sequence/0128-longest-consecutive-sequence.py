class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        if len(nums)==0:
            return 0
        curc=0
        resc=1
        for i in (sets):
            
            if i-1 in sets:
                continue
            else:
                curc=1
                ele=i
                while (ele+1 in sets):
                    curc+=1
                    ele+=1
                resc = max(resc,curc)
        return resc

            
