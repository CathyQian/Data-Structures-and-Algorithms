"""
Maximum Length of Repeated Subarray

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].

 

Note:

    1 <= len(A), len(B) <= 1000
    0 <= A[i], B[i] < 100

"""
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        maxlen = 0
        m, n = len(A), len(B)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    maxlen = max(dp[i+1][j+1], maxlen)
        return maxlen