"""
Maximum Length of Repeated Subarray
"""
# solution -- dp
class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n, m = len(A), len(B)
        length = 0 
        f = [[0 for x in range(n + 1)] for y in range(m + 1)]
        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    f[i+1][j+1] = f[i][j] + 1
                    length = max(length, f[i+1][j+1])
                else:
                    f[i+1][j+1] = 0
        return length