"""
Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:

    You may assume that the matrix does not change.
    There are many calls to sumRegion function.
    You may assume that row1 ≤ row2 and col1 ≤ col2.

"""


# (0,0)
# ---------------------------
# |                         |
# |           (r1,c1)       |
# |             |-----------|(r1,c2)
# |             |  RegionA  |
# | ------------------------|(r2,c2)
# |           (r2,c1)       |
#  --------------------------
#  RegionA = region(0,0 to r2,c2) - 
#       region(0,0 to r2,c1) - 
#       region(0,0 to r1,c2) + 
#       region(0,0 to r1,c1)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.nrow = len(matrix)
        self.ncol = len(matrix[0]) if self.nrow > 0 else 0

        self.sum = [[0 for i in range(self.ncol)] for j in range(self.nrow)]
        for i in range(self.nrow):
            for j in range(self.ncol):
                left = self.sum[i][j - 1] if j > 0 else 0
                top = self.sum[i - 1][j] if i > 0 else 0
                topleft = self.sum[i - 1][j - 1] if i > 0 and j > 0 else 0
                self.sum[i][j] = matrix[i][j] + top + left - topleft
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.sum[row2][col1 - 1] if col1 > 0 else 0
        top = self.sum[row1 - 1][col2] if row1 > 0 else 0
        topleft = self.sum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.sum[row2][col2] + topleft - top - left

