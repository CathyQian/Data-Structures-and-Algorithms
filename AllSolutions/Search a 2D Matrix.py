"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
# binary search, treat 2D array as 1D array
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r-l)//2
            row, col = mid // n , mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
