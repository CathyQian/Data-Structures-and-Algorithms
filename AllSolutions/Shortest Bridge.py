"""
Shortest Bridge

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.


"""
# BFS to find minimum steps
# time and space complexity O(mn)
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        island1 = []
        for i in range(len(grid)):
            if len(island1) > 0: # cannot use if not island1
                break
            for j in range(len(grid[0])):
                if grid[i][j] == 1: # found one island
                    self.findLands(grid, i, j, island1) #island1 is a list, mutable, so can be brought into the list; if immutable, no
                    break
        d = deque(island1)
        d.append(('#', '#'))
        steps = 0
        while d and d != deque([("#", '#')]):
            (col, row) = d.popleft()
            while (col, row) != ('#', '#'):
                for x, y in [(col-1, row), (col+1, row), (col, row-1), (col, row+1)]:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                        if grid[x][y] == 0:
                            grid[x][y] = '*' # mask
                            d.append((x, y))
                        elif grid[x][y] == 1: # this must come from island2
                            return steps
                (col, row) = d.popleft()
            d.append(('#', '#'))
            steps += 1
        return -1 # if not found

    def findLands(self, grid, col, row, island1):
        island1.append((col, row))
        grid[col][row] = '#' # mask, no recover afterwards
        for x, y in [(col-1, row), (col+1, row), (col, row-1), (col, row+1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                self.findLands(grid, x, y, island1) 