"""
Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one
bomb. You can only place the bomb in an empty cell.

The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 500
    grid[i][j] is either 'W', 'E', or '0'.

"""

# brutal force, O(m*n*(m+n))

# simplified, O(m*n)
class Solution(object):
    def maxKilledEnemies(self, grid):
        if len(grid) == 0:
            return 0
        max_hits = 0
        nums = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        #From Left
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'E':
                    row_hits += 1
                elif grid[i][j] == 'W':
                    row_hits = 0
                else:
                    nums[i][j] = row_hits
                
        #From Right
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] == 'W':
                    row_hits = 0
                elif grid[i][j] == 'E':
                    row_hits +=1
                else:
                    nums[i][j] += row_hits
        
        #From Top
        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums)):
                if grid[col][i] == 'E':
                    col_hits += 1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    nums[col][i] += col_hits
        
        #From Bottom
        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums)-1, -1, -1):
                if grid[col][i] == 'E':
                    col_hits +=1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    nums[col][i] += col_hits
                    max_hits = max(max_hits, nums[col][i])


        return max_hits