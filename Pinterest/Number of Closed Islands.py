"""
Number of Closed Islands
"""
"""
这道题很大的一个陷阱是直接从number of islands加边界条件改过来的答案是错误的。
因为number of islands会把扫描过的点标记为-1, 在这道题里面，需要判断某个点为0且是否触及边界，如果一个点事先被改为-1， 那么这个点
相当于提供了新的边界，所以最后结果比应得结果大。
"""
# wrong solution, how to correct
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if len(grid)-1 > i > 0 and len(grid[0])-1 > j > 0 and grid[i][j] == 0:
                    if self.dfs(grid, i, j):
                        count += 1
                        
        return count
    
    def dfs(self, grid, i, j):
        grid[i][j] = -1 # this line will add trouble to line 26 and line 28
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (i+x == 0 or i+x == len(grid)-1 or j+y == 0 or j+y == len(grid[0]) - 1) and (grid[i+x][j+y] == 0): # this line has some problems
                return False
            elif len(grid) - 1 > i+x > 0 and len(grid[0]) - 1 > j+y > 0 and grid[i+x][j+y] == 0:
                res = self.dfs(grid, i+x, y+j)
                if not res:
                    return False
        return True

# the correct solution, do dfs from edge 0 and convert all accessible elements to 1, then do dfs from non-edge elements
# and count
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        for j in range(0, n):
            if grid[0][j] == 0:
                self.dfs(grid, 0, j)
            if grid[m-1][j] == 0:
                self.dfs(grid, m-1, j)
        for i in range(1, m-1):
            if grid[i][0] == 0:
                self.dfs(grid, i, 0)
            if grid[i][n-1] == 0:
                self.dfs(grid, i, n-1)
        count = 0
        for i in range(1, m-1):
            for j in range(1, n-1): 
                if grid[i][j] == 0:
                    self.dfs(grid, i, j)
                    count += 1             
        return count
    
    def dfs(self, grid, i, j):
        grid[i][j] = 1
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if len(grid) > i+x >= 0 and len(grid[0]) > j+y >= 0 and grid[i+x][j+y] == 0:
                self.dfs(grid, i+x, y+j)
