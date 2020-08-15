"""
Longest Increasing Path in a Matrix

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo, maxlength = {}, 0 # maxlength in main function
        for i in range(m):
            for j in range(n):
                length = self.dfs(matrix, i, j, memo)
                maxlength = max(maxlength, length)
        return maxlength
    
    def dfs(self, matrix, row, col, memo):
        if (row, col) not in memo:
            ans = 1 # local variable to record max length 
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= row+x < len(matrix) and 0 <= col+y < len(matrix[0]) and matrix[row+x][col+y] > matrix[row][col]:   
                    length = self.dfs(matrix, row+x, col+y, memo)
                    ans = max(ans, length+1)
            memo[(row, col)] = ans # local maximum
        return memo[(row, col)]