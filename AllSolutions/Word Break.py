"""
Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into
a space-separated sequence of one or more dictionary words.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


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
 
# recursion with memory, pay special attention to r direction, O(n2) --- scan each word s[i:j] to see if it exist in wordDict and memorize it
# Using memo or not: many duplicated operation --> yes, otherwise no
class Solution(object):
    def wordBreak(self, s, wordDict):  
        memo = {len(s): True} # stop condition
        return self.canBreak(s, 0, memo, set(wordDict))
    
    def canBreak(self, s, start, m, wordDict):
        # m[start]: bool, indicate if s[start:] can be broken as desired or not
        if start not in m:
            m[start] = False # initialize!
            if s[start:] in wordDict: 
                m[start] = True
            else:
                for i in range(start+1, len(s)):             
                    if s[start:i] in wordDict and self.canBreak(s, i, m, wordDict):
                        m[start] = True
                        break
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

