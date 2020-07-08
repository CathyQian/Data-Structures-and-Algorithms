"""
[Leetcode](https://leetcode.com/problems/word-search-ii/)

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

 

Note:

    All inputs are consist of lowercase letters a-z.
    The values of words are distinct.

"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a Trie based on words, to allow for easy search
        root = {}
        self.keyword = '*'
        for word in words:
            node = root # initialize node for each word
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[self.keyword] = word
        if len(board) == 0:
            return []
        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root:
                    self.dfs(board, i, j, root, result)
        return result

    def dfs(self, board, row, col, parent, result):
        char = board[row][col]
        child = parent[char]

        if self.keyword in child:
            result.append(child.pop(self.keyword)) # pop to allow no duplicates in results
        
        if child: # if this node is visited before, then child will be empty
            board[row][col] = '#' # same node can't be visited twice
            for i, j in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                if 0 <= row + i < len(board) and 0 <= col + j < len(board[0]) and board[row+i][col+j] in child:
                    self.dfs(board, row+i, col+j, child, result)
            board[row][col] = char

