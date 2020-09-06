"""
Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]


"""

# dfs + memo (memo vals are different from word break I; dfs needs res to record path)
class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.dfs(s, 0, wordDict, dict())
    
    def dfs(self, s, start, wordDict, memo):
        """return breaking combination of s[start:] in memo[start] (equivalent to res)
        """
        if start == len(s): # test edge case
            return [""]
        if start not in memo:
            res = [] # needed to record path along the recursion process, the main difference from Word Break
            for word in wordDict:
                if start + len(word) <= len(s) and s[start:start+len(word)] == word:
                    for r in self.dfs(s, start+len(word), wordDict, memo):
                        res.append(word + ("" if not r else " " + r))
            memo[start] = res
        return memo[start]
"""
