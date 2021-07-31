"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.


"""

# Method 1: Top-Down dp + dp
class Solution:
    def minCut(self, s: str) -> int:
        dp1 = [[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if j == i:
                    dp1[j][i] = True
                else:
                    if s[j] == s[i]:
                        dp1[j][i] = (i-j) == 1 or dp1[j+1][i-1]
        dp2 = [i for i in range(len(s))]
        for i in range(1, len(s)):
            for j in range(i+1):
                if dp1[j][i]:
                    if j == 0:
                        dp2[i]=0
                    else:
                        dp2[i] = min(dp2[j-1] + 1, dp2[i])
        return dp2[-1]

# Method 2: Memoization
class Solution:
    def minCut(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i)[::-1]:
                if s[j] == s[i]:
                    dp[j][i] = (i-j == 1) or dp[j+1][i-1]
        self.memo = {}
        self.memo[len(s)] = -1
        return self.dfs(s, 0, dp)
    
    def dfs(self, s, start, dp):
        if start not in self.memo:
            ans = len(s) - start
            for i in range(start, len(s)):
                if dp[start][i] == True:
                    ans = min(ans, self.dfs(s, i+1, dp) + 1)
            self.memo[start] = ans
        return self.memo[start]

"""
key point: create the map based on the palindrome condition and find the shortest path.
1. dp could be applied to creat the map based the panlindrome condition
2. shortest path could be solved by bfs or dp
3. state transition for the second dp is if dp[i][j]: then dp[j] = min(dp[i-1]+1, dp[j])
"""
