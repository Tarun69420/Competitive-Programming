class Solution:
    def removeDuplicates(self, l: List[int]) -> int:
        left = 0
        
        for i in range(1,len(l)):
            if l[i]!=l[left]:
                left+=1
                l[left]=l[i]
        return left+1
            