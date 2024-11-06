from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle by modifying `board` in-place.
        """
        self.bs(board, 0, 0)
        
    def bs(self, board: List[List[str]], row: int, col: int) -> bool:
        # If we have completed all rows, the board is solved
        if row == 9:
            return True
        # If we have reached the end of the row, move to the next row
        if col == 9:
            return self.bs(board, row + 1, 0)
        # If cell is not empty, move to the next cell in the row
        if board[row][col] != ".":
            return self.bs(board, row, col + 1)
        
        # Try placing numbers 1-9 in the empty cell
        for num in range(1, 10):
            if self.valid(board, row, col, str(num)):
                board[row][col] = str(num)
                if self.bs(board, row, col + 1):  # Recur with the next column
                    return True
                board[row][col] = "."  # Backtrack if placing num didn't work
        return False  # No valid number could be placed in this cell

    def valid(self, board: List[List[str]], row: int, col: int, num: str) -> bool:
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
