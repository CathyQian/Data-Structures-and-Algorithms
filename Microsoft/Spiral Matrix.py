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

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix:
            temp = []
            nC, nR =  len(matrix[0]), len(matrix)
            if nR > nC:
                iterate = 2 * nC
            else:iterate = 2 * nR - 1
            iterate = iterate // 4 + 1
            for i in range(iterate):
                for j in range(i, nC-i):
                    temp.append(matrix[i][j])
                if len(temp) == nC * nR:
                    break
                for j in range(1+i, nR-i):
                    temp.append(matrix[j][nC-1-i])
                if len(temp) == nC * nR:
                    break
                for j in range(nC-2-i,-1+i,-1):
                    temp.append(matrix[nR-1-i][j])
                if len(temp) == nC * nR:
                    break
                for j in range(nR-2-i, i, -1):
                    temp.append(matrix[j][i])
                if len(temp) == nC * nR:
                    break
            return temp
        else:return matrix