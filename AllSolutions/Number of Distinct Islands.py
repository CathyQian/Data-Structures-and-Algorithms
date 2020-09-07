"""
Number of Distinct Islands

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges
of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the
other.

Example 1:

11000
11000
00011
00011

Given the above grid map, return 1.

Example 2:

11011
10000
00001
11011

Given the above grid map, return 3.

Notice that:

11
1

and

 1
11

are considered different island shapes, because we do not consider reflection / rotation.

Note: The length of each dimension in the given grid does not exceed 50. 
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

