"""
[200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if len(grid) == 0:
            return 0
        self.row, self.col = len(grid), len(grid[0])
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j) # don't need to use self.grid as grid is a matrix that will be changed in dfs
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
        grid[i][j] = '#'
        for x, y in [(1,0), (-1,0), (0, 1), (0, -1)]:
            if 0<=i+x < self.row and 0<=j+y<self.col and grid[i+x][j+y] == '1':
                self.dfs(grid, i+x, j+y)
        