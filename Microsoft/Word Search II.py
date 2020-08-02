"""
Word Search II

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

# use trie, or else will show time exceed limit
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        if not board or not board[0]:
            return res
        
        # build the trie
        root = {}
        self.keyword = '*'
        for word in words:
            node = root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[self.keyword] = word
        
        # search for target in trie
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root:
                    self.dfs(board, i, j, root, res)                 
        return sorted(res)
    
    def dfs(self, board, row, col, parent, res):
        char = board[row][col]
        child = parent[char]
        if self.keyword in child: # one word only recorded once
            res.append(child.pop(self.keyword))
        if child: # not elif!!!
            board[row][col] = '#'
            for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if x+row >= 0 and x+row < len(board) and y+col >= 0 and y+col < len(board[0]) and board[x+row][y+col] in child:
                    self.dfs(board, x+row, y+col, child, res)               
            board[row][col] = char
            