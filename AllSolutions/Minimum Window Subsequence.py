"""
Minimum Window Subsequence

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.

 

Note:

    All the strings in the input will only contain lowercase letters.
    The length of S will be in the range [1, 20000].
    The length of T will be in the range [1, 100].

 
"""
# dynamic programming
# f[i] updates the starting positions in S such that the substring T[ : i+1] all appears in S[f[i]:j] (j is the scanning index in S).
# An extra dictionary is used to facilitate the lookup of potential appearance of letters in T for a given letter in S.

import collections
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        f = [len(S)+1]*len(T)
        
        dic = collections.defaultdict(list)
        for i, c in enumerate(T):
            dic[c].append(i)
        
        for k in dic: # need to reverse because f[j] is updated based on f[j-1]
            dic[k].reverse()  
            
        ans_l = len(S) + 1
        ans = ""
        for i, c in enumerate(S):
            if c in dic:
                # this part is tricky
                for j in dic[c]: # [5,3,0]
                    if j == 0:
                        f[j] = i
                    else:
                        f[j] = f[j-1]
            
            if f[-1] < len(S) + 1 and (i - f[-1] + 1 < ans_l): # min length
                ans_l = i - f[-1] + 1
                ans = S[f[-1]:i+1]
                
        return ans

# https://www.cnblogs.com/grandyang/p/8684817.html
# method 2, dp, slower but easier to understand
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        m, n = len(S), len(T)
        start, minlen = -1, len(S)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)] # dp[i][j] starting point of S[:i+1] and T[:j+1], if -1 no match
        for i in range(m+1):
            dp[i][0] = i
            
        for i in range(1, m+1):
            for j in range(1, min(i, n) + 1): # j <= n and j <= i
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
                    
            if dp[i][n] != -1:
                curlen = i - dp[i][n]
                if minlen > curlen:
                    minlen = curlen
                    start = dp[i][n]
        return "" if start == -1 else S[start:start+minlen]
        