"""
[74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

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
# method 1, treate the 2D matrix as a 1D sorted array, do binary search, time complexity O(m*n), space complexity O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m*n - 1
        while start <= end:
            mid = start + (end - start)//2
            val = matrix[mid//n][mid%n]
            if val == target:
                return True
            elif val < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

# 