"""
"""
[140. Word Break II](https://leetcode.com/problems/word-break-ii/)
"""
"""
# not sure why this method always give time exceed limit,

import collections

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = collections.defaultdict(set)
        wordDict = set(wordDict)
        self.dfs(s, 0, wordDict, memo)
        return memo[0]
    
    def dfs(self, s, start, wordDict, memo):
        if start != len(s):
            if s[start:] in wordDict:
                memo[start].add(s[start:])
            for word in wordDict:
                end = start + len(word)
                if s[start:end] == word and self.dfs(s, end, wordDict, memo):
                    memo[start].update(set([s[start:end] + ' ' + p for p in memo[end]]))
        return True if memo[start] else False
"""
class Solution(object):
    def wordBreak(self, s, wordDict):

        res = []
        memo = dict()
        return self.dfs(s, res, wordDict, memo)
    
    def dfs(self, s, res, wordDict, memo):
        if s in memo: return memo[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            if s[:len(word)] != word: continue
            for r in self.dfs(s[len(word):], res, wordDict, memo):
                res.append(word + ("" if not r else " " + r))
        memo[s] = res
        return res
"""