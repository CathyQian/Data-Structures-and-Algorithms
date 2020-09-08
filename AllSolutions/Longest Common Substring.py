# Lintcode 79
Given two strings, find the longest common substring.

Return the length of it.


Example
Example 1:
	Input:  "ABCD" and "CBCE"
	Output:  2
	
	Explanation:
	Longest common substring is "BC"


Example 2:
	Input: "ABCD" and "EACB"
	Output:  1
	
	Explanation: 
	Longest common substring is 'A' or 'C' or 'B'
Challenge
O(n x m) time and memory.

class Solution:
    def longestSubstring(self, s1, s2):
	if not s1 or not s2:
	    return 0
	m, n = len(s1), len(s2)
	ans = 0
	dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
	for i in range(m):
	    for j in range(n):
		if s1[i] == s2[j]:
		    dp[i+1][j+1] = dp[i][j] + 1
		    ans = max(ans, dp[i+1][j+1])
		else: # major difference from subsequence
		    dp[i+1][j+1] = 0
        return ans
