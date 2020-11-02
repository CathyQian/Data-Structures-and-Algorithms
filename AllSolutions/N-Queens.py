"""
N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

"""
# recursion with backtracking

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        self.placeQueens(board, 0, res)
        return res

    def placeQueens(self, board, row, res):
        if row == self.n:
            res.append([''.join(x) for x in board])
        for col in range(self.n):
            if self.isSafe(board, row, col):
                board[row][col] = "Q"
                self.placeQueens(board, row + 1, res)
                board[row][col] = "." # backtracking part

    def isSafe(self, board, row, col):
        for r in range(row):
            if board[r][col] == "Q":
                return False

        # check upper left diagonal
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[r][c] == "Q":
                return False

        # check upper right diagonal
        for r, c in zip(range(row, -1, -1), range(col, self.n)):
            if board[r][c] == "Q":
                return False
        return True