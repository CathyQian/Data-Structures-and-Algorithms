"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Example 1:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:
Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

# method 1: O(mn) time complexity， O(1) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    for k in range(n):
                        if matrix[r][k] != 0:
                            matrix[r][k] = '#'
                    for k in range(m):
                        if matrix[k][c] != 0:
                            matrix[k][c] = '#'
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '#':
                    matrix[r][c] = 0
        

# method 2: O(m+n) space,  O(mn) time
class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
