"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following 
properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

# Solution 1: efficient search, this is different from binary search though. O(m + n)
# This is a classical way to search in partially ordered matrix. You can start
# from matrix[m-1][n-1] or matrix[m-1][0] or matrix[0][n-1] or matrix[0][0]. 
# Be adaptive to the problem. Don't always stick to binary search. Indeed, binary
# search won't work well here since it will over-filter elements.
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # be careful with extreme cases
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False

        row, col = len(matrix), len(matrix[0])
        cr, cc = 0, col - 1
        while cr < row and cc >= 0:
            if matrix[cr][cc] == target:
                return True
            elif matrix[cr][cc] > target:
                cc -= 1
            else:
                cr += 1

        return False
        
# Solution 2: divide and conquer, O(nlogn) time
# This is a smart binary search. Very easy to make mistakes though.
# ref:https://www.geeksforgeeks.org/search-in-a-row-wise-and-column-wise-sorted-2d-array-using-divide-and-conquer-algorithm/
# the following code have some bug in the index 
class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        row, col = len(matrix), len(matrix[0])
        start_row, end_row = 0, row - 1
        start_col, end_col = 0, col - 1

        while start_row < end_row - 1 and start_col < end_col - 1:
            mid_row = start_row + (end_row - start_row)//2
            mid_col = start_col + (end_col - start_col)//2
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                result1 = self.searchMatrix(matrix[start_row : mid_row + 1][mid_col + 1 : end_col + 1], target) 
                result2 = self.searchMatrix(matrix[mid_row + 1: end_row + 1][start_col : end_col + 1], target)
                return result1 or result2
            else:
                result3 = self.searchMatrix(matrix[mid_row: end_row + 1][start_col : mid_col], target) 
                result4 = self.searchMatrix(matrix[start_row: mid_row][start_col : end_col + 1], target)
                return result3 or result4
        
        # deal with start_row = end_row - 1 or start_col = end_col - 1
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                if matrix[i][j] == target:
                    return True
        
        return False