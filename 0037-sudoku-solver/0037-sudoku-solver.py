from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle by modifying `board` in-place.
        """
        self.solve(board)
        
    def solve(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":  # Find an empty cell
                    for num in range(1, 10):
                        if self.is_valid(board, row, col, str(num)):
                            board[row][col] = str(num)  # Place the number
                            if self.solve(board):  # Recur for next cell
                                return True
                            board[row][col] = "."  # Backtrack
                    return False  # No valid number, return False
        return True  # Solved the board

    def is_valid(self, board: List[List[str]], row: int, col: int, num: str) -> bool:
        # Check the row
        for i in range(9):
            if board[row][i] == num:
                return False
        # Check the column
        for i in range(9):
            if board[i][col] == num:
                return False
        # Check the 3x3 sub-grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True
