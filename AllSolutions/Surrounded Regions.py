"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the
border of the board are not flipped to 'X'. Any 'O' that is not on the border and
it is not connected to an 'O' on the border will be flipped to 'X'. Two cells
are connected if they are adjacent cells connected horizontally or vertically.
"""

"""
Solution: search 'O' among edge elements, if found, change it into 'y', then do dfs around to find '0'
after finish, change all 'O' into 'X' and all 'y' into 'O'
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if board is None or len(board) < 3 or len(board[0]) < 3:
            return
        m, n = len(board), len(board[0])
        
        # do DFS to all border O
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][n-1] == 'O':
                self.dfs(board, i, n-1)
                
        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[m-1][j] == 'O':
                self.dfs(board, m-1, j)
        
        # convert all y to O, all O to X
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return
    
    def dfs(self, board, i, j):
        # dfs to board[i][j], when find 'O', convert to y
        
        board[i][j] = 'y'
        m, n = len(board), len(board[0])
        
        if i - 1 >= 0 and board[i-1][j] == 'O':
            self.dfs(board, i-1, j)
        
        if i + 1 <= m-1 and board[i+1][j] == 'O':
            self.dfs(board, i+1, j)
        
        if j - 1 >= 0 and board[i][j-1] == 'O':
            self.dfs(board, i, j-1)
        
        if j + 1 <= n-1 and board[i][j+1] == 'O':
            self.dfs(board, i, j+1)
        
        return