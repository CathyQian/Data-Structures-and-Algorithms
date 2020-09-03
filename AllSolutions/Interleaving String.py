"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false


"""
# dp[i][j] true or false of s1[:i] and s2[:j] to make up s3[:i+j]
# dp[i][0] and dp[0][j] can be initialized easily, dp[0][0] = True
# dp[i+1][j+1] = (dp[i][j+1] and s1[i]==s3[i+j+1] ) or (dp[i+1][j] and s2[j]==s3[i+j+1] )
# return dp[len(s1)][len(s2)]

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m): 
            dp[i+1][0] = (dp[i][0] and (s1[i] == s3[i]))
        for j in range(n):
            dp[0][j+1] = (dp[0][j] and (s2[j] == s3[j])) 
        for i in range(m):
            for j in range(n):
                 dp[i+1][j+1] = (dp[i][j+1] and s1[i] == s3[i+j+1]) or (dp[i+1][j] and s2[j] == s3[i+j+1])
        return dp[m][n]