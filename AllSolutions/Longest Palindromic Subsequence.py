"""
 Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"

Output:

4

One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:

"cbbd"

Output:

2

One possible longest palindromic subsequence is "bb". 
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n)[::-1]:
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

# change scan direction
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            for j in range(i-1, -1, -1):
                if s[j] == s[i]:
                    dp[j][i] = dp[j+1][i-1] + 2
                else:
                    dp[j][i] = max(dp[j+1][i], dp[j][i-1])
        return dp[0][n-1]
"""   
Idea:
- This problem is quite similar to find longest Palindromic subsequence (iterate through each element, 
for each element, search both left and right for the same element). The difference here is that it's 
looking for subsequence which the elements doesn't need to be adjacent to each other.

- For such types of questions where min/max number of combinations is needed, dynamic programming is a top choice.
- For dp,let's define
 - state: dp[i][j] represents the longest palindromic subsequence between s[i] and s[j], including s[i] and s[j]
 - function:
 if s[i]=s[j], dp[i][j] = dp[i+1][j-1]+2
 if s[i]!=s[j], dp[i][j] = max(dp[i+1][j], dp[i][j-1]) (this relationship is where I find difficult. For substring, 
 since all elements needs to be adjacent, this relationship is not true anymore)
 """
