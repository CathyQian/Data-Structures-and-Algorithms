"""
Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

 

Constraints:

    board and word consists only of lowercase and uppercase English letters.
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3

"""

# DFS
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word):
                        return True
        return False
    
    def dfs(self, board, i, j, word):
        if len(word) == 1:
            return True
        temp = board[i][j]
        board[i][j] = '#'
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0<=i+x<len(board) and 0<=j+y<len(board[0]) and board[i+x][j+y] == word[1]:
                if self.dfs(board, i+x, j+y, word[1:]):
                    return True
        board[i][j] = temp
        return False
