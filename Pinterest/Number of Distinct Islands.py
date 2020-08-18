"""
Number of Distinct Islands
"""
"""
If islands has the same landscape, then its neighboring environment should be exactly the same. So use DFS to probe the path will
result in exactly the same path. 

At each point, collect up, down, left, right path, make sure to go back to original points before probing the next direction.
The interval directional words can't be ignored. Or else, one unique path may map to multiple islands with different shapes.

"""

class Solution:
    def numDistinctIslands(self, grid):
        islands = set([])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    islands.add(self.dfs(grid, i, j, "s"))

        return len(islands)

    def dfs(self, g, i, j, path):
        if i < 0 or j < 0 or i >= len(g) or j >= len(g[i]) or g[i][j] == 0:
            return ""

        g[i][j] = 0
        return path + self.dfs(g, i+1, j, "d") + "u" \
               + self.dfs(g, i-1, j, "u") + "d"  \
               + self.dfs(g, i, j+1, "r") + "l"\
               + self.dfs(g, i, j-1, "l") + "r"

