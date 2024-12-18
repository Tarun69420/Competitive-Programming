class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        ans = []
        n = len(digits)
        d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def bs(digits,ans,s):
            if len(digits) == 0:
                ans.append(s)
                return
            
            for j in d[digits[0]]:
                    bs(digits[1:],ans,s+j)
        bs(digits,ans,"")
        return ans
            