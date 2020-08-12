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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return None
        # build a trie to allow for easy word path search
        root = {}
        self.keyword = "*"
        for word in words:
            node = root
            for w in word:
                if w not in node:
                    node[w] = {}
                node = node[w]
            node[self.keyword] = word # indicating end of a word
        
        # use bfs to search for word in board
        self.res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root:
                    self.dfs(board, i, j, root)
               
        return self.res
    
    def dfs(self, board, i, j, parent):
        char = board[i][j]
        child = parent[char]
        # a word is found
        if self.keyword in child: 
            self.res.append(child.pop(self.keyword))
        # continue searching along the same path to see if other words can be found
        if child:
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i+x < len(board) and 0 <= j+y < len(board[0]) and board[i+x][j+y] in child:
                    board[i][j] = '#' # don't forget this step
                    self.dfs(board, i+x, j+y, child)
                    board[i][j] = char # don't forget this step