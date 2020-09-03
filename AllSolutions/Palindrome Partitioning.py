"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
# dfs
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, 0, [], res)
        return res
    
    def dfs(self, s, start, path, res):
        
        if start == len(s):
            res.append(path)
        
        for i in range(start, len(s)):
            if s[start:i+1] == s[start:i+1][::-1]:
                self.dfs(s, i+1, path + [s[start:i+1]], res)
        
    
# dfs + dp

Method2: dfs+dp
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False for _ in s] for _ in s]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i)[::-1]:
                if s[j] == s[i]:
                    dp[j][i] = i-j==1 or dp[j+1][i-1]
        
        result = []
        self.dfs(result, [], s, 0, dp)
        return result 

    def dfs(self, result, base, s, start, dp):
        if start == len(s):
            if base:
                result.append(base)
        
        for i in range(start, len(s)):
                if dp[start][i] == True:
                    self.dfs(result, base+[s[start:i+1]], s, i+1, dp)
        return

# dp[i][j]: s[i:j+1] is Palindrome or not
# base condition: dp[i][i] = True, everything else False
# state transition: dp[i][j] = (j-i == 1 or dp[i+1][j-1]) if s[i] == s[j]

# dp is used to tell if s[i][j] is palindrome