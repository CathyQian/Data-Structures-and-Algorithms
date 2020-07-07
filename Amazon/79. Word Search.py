"""
[Leetcode](https://leetcode.com/problems/word-search/)

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
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.row, self.col = len(board), len(board[0])
        for i in range(self.row):
            for j in range(self.col):
                if word[0] == board[i][j]:
                    if self.dfs(board, i, j, word[1:]):
                        return True
        return False
    
    
    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        prefix = board[i][j]
        board[i][j] = '#'
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = False
        for x, y in directions:
            if i+x >= 0 and i+x < self.row and j+y >= 0 and j+y < self.col and board[i+x][j+y] == word[0]:
                result = self.dfs(board, i+x, j+y, word[1:])
                if result:
                    break
        board[i][j] = prefix
        return result