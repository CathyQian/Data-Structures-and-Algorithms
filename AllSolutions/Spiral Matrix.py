"""
Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""
# https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/178 
# key: update index at every step and stop when index condition violated.If there is any unvisited element, up<=down & left <= right
# if one of such condition is violated, then no unvisited element, stop loop and return
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return None # not return null
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m-1, 0, n-1
        res = []
        while up <= down and left <= right:
            for i in range(left, right+1):
                res.append(matrix[up][i])      
            up += 1
            if up > down: # required
                break
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left: # required
                break
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1
            if up > down: # required
                break
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1
            if right < left: # required
                break
        return res


"""
Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


"""
# similar logic as before
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[]]
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        up, down, left, right = 0, n-1, 0, n-1
        val = 1
        while up <= down and left <= right:
            for i in range(left, right+1):
                matrix[up][i] = val
                val += 1
            up += 1
            if up > down: # required
                break
            for i in range(up, down + 1):
                matrix[i][right] = val
                val += 1
            right -= 1
            if right < left: # required
                break
            for i in range(right, left-1, -1):
                matrix[down][i] = val
                val += 1
            down -= 1
            if up > down: # required
                break
            for i in range(down, up-1, -1):
                matrix[i][left] = val
                val += 1
            left += 1
            if right < left: # required
                break
        return matrix