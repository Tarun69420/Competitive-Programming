class Solution:
    def removeDuplicates(self, l: List[int]) -> int:
        pre=l[0]
        k=1
        i=1
        n=len(l)
        while(i<n):
            
            cur=l[i]
            
            if cur==pre:
                l.append(l.pop(i))
                i-=1
                n-=1
            else:
                #print(k,l)
                pre=cur
                k+=1
            i+=1
        return k
            