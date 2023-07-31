"""
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

 

Example 1:


Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]
Example 2:

Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]
 

Constraints:

m == mat1.length
k == mat1[i].length == mat2.length
n == mat2[i].length
1 <= m, n, k <= 100
-100 <= mat1[i][j], mat2[i][j] <= 100
"""

# regular matrix multiplication, time complexity: O(nmk)
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        if not mat1 or not mat1[0] or not mat2 or not mat2[0]:
            return None
        m, k = len(mat1), len(mat1[0])
        j, n = len(mat2), len(mat2[0])
        if k != j:
            return None
        res = [[0] * n for _ in range(m)] # m*n

        for i in range(m):
            for j in range(n):
                for h in range(k):
                    res[i][j] += mat1[i][h] * mat2[h][j]
        return res

# take advantage of sparisty, much faster
import collections 
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        if not mat1 or not mat1[0] or not mat2 or not mat2[0]:
            return None
        m, k = len(mat1), len(mat1[0])
        j, n = len(mat2), len(mat2[0])
        if k != j:
            return None
        
        res = [[0] * n for _ in range(m)] # m*n

        mat1_dic, mat2_dic = collections.defaultdict(dict), collections.defaultdict(dict)
        # O(mk)
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    mat1_dic[j][i] = mat1[i][j] # index are reversely stored
        # O(nk)
        for i in range(k):
            for j in range(n):
                if mat2[i][j] != 0:
                    mat2_dic[i][j] = mat2[i][j]
        
        # find (i, k) and (k, j) in hashmap --> add multiplication to res[i][k]
        #O(kmn) worst case scenario
        for h in range(k):
            if h in mat1_dic and mat2_dic:
                for i in mat1_dic[h]:
                    for j in mat2_dic[h]:
                        res[i][j] += mat1_dic[h][i] * mat2_dic[h][j]

        return res
