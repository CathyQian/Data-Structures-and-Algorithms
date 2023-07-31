"""
Maximum Non Negative Product in a Matrix

You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 10^9 + 7. If the maximum product is negative, return -1.

Notice that the modulo is performed after getting the maximum product.

Example 1:
Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
Output: -1
Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.

Example 2:
Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).

Example 3:
Input: grid = [[1,3],[0,-4]]
Output: 0
Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
-4 <= grid[i][j] <= 4

"""

# DFS, time exceed limit

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        self.maxprod = -1
        self.dfs(grid, 0, 0, grid[0][0])
        return -1 if self.maxprod < 0 else self.maxprod%(10**9 + 7)

    def dfs(self, grid, i, j, cur):
        # exit condition
        if i == len(grid) - 1 and j == len(grid[0]) - 1 and cur >= 0:
            self.maxprod = max(self.maxprod, cur)
        else:
            for x, y in [(i+1, j), (i, j+1)]: # only move right or down
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    self.dfs(grid, x, y, cur*grid[x][y])
        return
    
    # DP1

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None) #  helps in reducing the execution time of the function by using memoization technique; remove this line will result in Time Exceed Limit
        def fn(i, j): 
            """Return maximum & minimum products ending at (i, j)."""
            if i == 0 and j == 0: 
                return grid[0][0], grid[0][0]
            if i < 0 or j < 0: 
                return -inf, inf
            if grid[i][j] == 0: 
                return 0, 0
            mx1, mn1 = fn(i-1, j) # from top
            mx2, mn2 = fn(i, j-1) # from left 
            mx, mn = max(mx1, mx2)*grid[i][j], min(mn1, mn2)*grid[i][j] #???? if we are considering absolute values?
            return (mx, mn) if grid[i][j] > 0 else (mn, mx)
        
        mx, _ = fn(m-1, n-1)
        return -1 if mx < 0 else mx % (10**9+7)
        
# DP2, slightly slower than DP1
class Solution:
    def maxProductPath(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        Max = [[0] * n for _ in range(m)]
        Min = [[0] * n for _ in range(m)]
        Max[0][0], Min[0][0] = A[0][0], A[0][0]
        for j in range(1, n):
            Max[0][j] = Max[0][j - 1] * A[0][j]
            Min[0][j] = Min[0][j - 1] * A[0][j]

        for i in range(1, m):
            Max[i][0] = Max[i - 1][0] * A[i][0]
            Min[i][0] = Min[i - 1][0] * A[i][0]

        for i in range(1, m):
            for j in range(1, n):
                Max[i][j] = max(Max[i - 1][j], Max[i][j - 1]) * A[i][j]
                Min[i][j] = min(Min[i - 1][j], Min[i][j - 1]) * A[i][j]
                if A[i][j] < 0:
                    Max[i][j], Min[i][j] = Min[i][j], Max[i][j]
        
        return Max[m-1][n-1] % (10**9 + 7) if Max[m-1][n-1] >= 0 else -1