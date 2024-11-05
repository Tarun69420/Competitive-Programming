from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]
        self.solve(0, n, board, ans)
        return ans

    def solve(self, col: int, n: int, board: List[List[str]], ans: List[List[str]]):
        if col == n:  # All queens are placed
            solution = ["".join(row) for row in board]
            ans.append(solution)
            return
        
        for row in range(n):
            if self.safe(row, col, board, n):
                board[row][col] = "Q"  # Place the queen
                self.solve(col + 1, n, board, ans)  # Move to the next column
                board[row][col] = "."  # Backtrack

    def safe(self, row: int, col: int, board: List[List[str]], n: int) -> bool:
        # Check upper-left diagonal
        r, c = row, col
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        # Check left row
        c = col
        while c >= 0:
            if board[row][c] == "Q":
                return False
            c -= 1

        # Check lower-left diagonal
        r, c = row, col
        while r < n and c >= 0:
            if board[r][c] == "Q":
                return False
            r += 1
            c -= 1

        return True
