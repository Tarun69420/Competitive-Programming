class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.bs(board,word,i,j,set()):
                    return True
        return False
    def bs (self,board,word,i,j,visit):
        if word == "":
            return True
        if (i,j) in visit or i>=len(board) or j>=len(board[0]) or i<0 or j<0 or board[i][j]!=word[0]:
            return False

        visit.add((i,j))
        if self.bs(board,word[1:],i,j+1,visit) == True:
                return True
        if self.bs (board,word[1:],i+1,j,visit) == True:
                return True
        if self.bs (board,word[1:],i-1,j,visit) == True:
                return True
        if self.bs (board,word[1:],i,j-1,visit) == True:
                return True
        visit.discard((i,j))
        
        return False
            
