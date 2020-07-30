"""
[240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

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

# searching space reduction such as binary search is a normal technique used in searching problems. But the key point is after 
# reducing the searching space, the remaining problem still has to be the same format compared to the original 
# problem, thus could be solved iteratively or recursively. 
# Can use binary search, time complexity O(logM) + O(logN), space complexity O(1)
# Simple solution is to use double pointer and walk step by step
# Time complexcity: O(N+M), Space complexity: O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # be careful with extreme cases, not matrix is not enough, [[]], [], [[None]]
        if not matrix or not matrix[0]:
            return False

        row, col = len(matrix), len(matrix[0])
        i, j = 0, col - 1
        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1

        return False