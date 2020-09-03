"""
[139. Word Break](https://leetcode.com/problems/word-break/)
"""

# method 1, brutal force using recursion, works, but too slow
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        return self.wordbreakhelper(s, wordDict)
    
    def wordbreakhelper(self, s, wordDict):
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                if i+1 == len(s):
                    return True
                res = self.wordBreak(s[i+1:], wordDict)
                if res:
                    return True
        return False
    
    # time: O(n^n)
    # space: O(n)
 
# recursion with memory, pay special attention to r direction, O(n2)
class Solution(object):
    def wordBreak(self, s, wordDict):   
        memo = {}
        return self.canBreak(s, 0, memo, set(wordDict))
    
    def canBreak(self, s, start, m, wordDict):
        # m[start] true or false or s[start:]
        if start not in m:
            m[start] = False # initialize!
            if s[start:] in wordDict: 
                m[start] = True
            else:
                for i in range(start+1, len(s)):             
                    if s[start:i] in wordDict and self.canBreak(s, i, m, wordDict):
                        m[start] = True
        return m[start]

"""
# dp 
class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        dp = [False]*(len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if s[k:i] in wordDict and dp[k]:
                    dp[i] = True
        return dp[-1]
"""


# [132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)

# dp + dfs (with memorization)
class Solution:

    def minCut(self, s: str) -> int:
        dp = [[False]*len(s) for i in range(len(s))]
        # for i in range(len(s)-1, -1, -1):
        #    for j in range(i, len(s)):
        #        if i == j:
        #            dp[i][j] = True
        #        elif i < j:
        #            if s[i] == s[j]:
        #                dp[i][j] = (j-i==1) or dp[i+1][j-1]
                     
        for j in range(len(s)): # i <= j
            for i in range(j+1)[::-1]:
                if i == j:
                    dp[i][j] = True
                else:
                    if s[i] == s[j]:
                        dp[i][j] = (j-i == 1) or dp[i+1][j-1]
        self.memo = {}
        self.memo[len(s)] = -1
        return self.dfs(0, s, dp)
    
    def dfs(self, start, s, dp):
        if start not in self.memo:
            ans = len(s) - start
            for i in range(start,len(s)):
                if dp[start][i] == True:
                    ans = min(ans, self.dfs(i+1, s, dp) + 1)
            self.memo[start] = ans
        return self.memo[start]
# dp + dp
"""
#Method 1: Top-Down dp + dp
class Solution:
    def minCut(self, s: str) -> int:
        dp1 = [[False]*len(s) for i in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i,len(s)):
                if i == j:
                    dp1[i][j]=True
                elif i < j:
                    if s[i] == s[j]:
                        dp1[i][j] = (j-i)==1 or dp1[i+1][j-1]
                    
                    
        dp2 = [i for i in range(len(s))]
        for i in range(1, len(s)):
            for j in range(i+1):
                if dp1[j][i]:
                    if j==0:
                        dp2[i]=0
                    else:
                        dp2[i] = min(dp2[j-1]+1, dp2[i])
        
        return dp2[-1]
