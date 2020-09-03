"""
Unique Paths III

On a 2-dimensional grid, there are 4 types of squares:

    1 represents the starting square.  There is exactly one starting square.
    2 represents the ending square.  There is exactly one ending square.
    0 represents empty squares we can walk over.
    -1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

 

Note:

    1 <= grid.length * grid[0].length <= 20

"""

# regular DFS divide and conquer
class Solution:
    def uniquePathsIII(self, grid):
        self.grid = grid
        self.row, self.col = len(grid), len(grid[0])
        todo = 0
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] != -1:
                    todo += 1
                if grid[i][j] == 1:
                    start_row = i
                    start_col = j
                if grid[i][j] == 2:
                    self.end_row = i
                    self.end_col = j
        return self.dfs(start_row, start_col, todo)
    
    def dfs(self, row, col, todo):
        if row == self.end_row and col == self.end_col and todo == 1:
            return  1
        else:
            ans = 0
            self.grid[row][col] = -1
            for r, c in [(row-1, col),(row+1, col),(row, col-1),(row, col+1)]:
                if 0 <= r < self.row and 0 <= c < self.col and self.grid[r][c]!= -1:
                    ans += self.dfs(r, c, todo-1)
            self.grid[row][col] = 0
            return ans

# DFS + Memoization + Bit manipulation(express the visited as an integer)
class Solution:
    def uniquePathsIII(self, grid):
        self.grid = grid
        self.row, self.col = len(grid), len(grid[0])
        self.memo = {}
        path = 0
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] %2 == 0:
                    path |= self.bitCode(i,j)
                if grid[i][j] == 1:
                    start_row = i
                    start_col = j
                if grid[i][j] == 2:
                    self.end_row = i
                    self.end_col = j
        return self.dfs(start_row, start_col, path)
    
    def bitCode(self, row, col):
        return 1 << (row*self.col + col)
    
    def dfs(self, row, col, path):
        if (row, col, path) not in self.memo:
            ans = 0
            if row == self.end_row and col == self.end_col:
                if path == 0:
                    ans += 1
            else:
                for r, c in [(row-1, col),(row+1, col),(row, col-1),(row, col+1)]:
                    if 0 <= r < self.row and 0 <= c < self.col and path&self.bitCode(r, c):
                            ans += self.dfs(r, c, path^self.bitCode(r, c))
            self.memo[(row,col,path)] = ans
        return self.memo[(row,col,path)]