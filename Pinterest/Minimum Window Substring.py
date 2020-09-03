"""
Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

"""
# https://www.cnblogs.com/grandyang/p/4340948.html
# key point: use hashmap, not hashset (find all characters, not find distinct characters)

import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        letterCnt = collections.defaultdict(int)
        left, cnt, minlen = 0, 0, sys.maxsize
        for c in t:
            letterCnt[c] += 1
        for i in range(len(s)): # right border of the window
            if s[i] in letterCnt:
                letterCnt[s[i]] -= 1
                if letterCnt[s[i]] >= 0: # this character is useful, otherwise, just an additional character
                    cnt += 1
            while cnt == len(t): # one window found, start to shrink window by sliding while keeping cnt == len(t)
                if minlen > i - left + 1:
                    minlen = i - left + 1
                    res = s[left:i+1]
                if s[left] in letterCnt: # left border of the window
                    letterCnt[s[left]] += 1
                    if letterCnt[s[left]] > 0:
                        cnt -= 1
                left += 1
        return res