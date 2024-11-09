from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        # Start search from every cell in the grid
        for i in range(rows):
            for j in range(cols):
                if self.bs(board, word, i, j, set()):
                    return True
        return False
    
    def bs(self, board, word, i, j, visit):
        # Base case: if word is empty, all characters have been matched
        if word == "":
            return True
        
        # Out of bounds, cell visited, or character mismatch
        if (i, j) in visit or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False

        # Mark the current cell as visited
        visit.add((i, j))
        
        # Recursively check all four possible directions
        if (self.bs(board, word[1:], i, j + 1, visit) or  # Right
            self.bs(board, word[1:], i + 1, j, visit) or  # Down
            self.bs(board, word[1:], i - 1, j, visit) or  # Up
            self.bs(board, word[1:], i, j - 1, visit)):   # Left
            return True

        # Backtrack: unmark the cell as visited
        visit.remove((i, j))
        
        return False
