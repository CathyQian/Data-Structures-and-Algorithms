"""
Longest Substring with At Most Two Distinct Characters

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        cur = collections.defaultdict(int)
        maxlen = 0
        start = 0
        for i, ss in enumerate(s):
            cur[ss] += 1
            while len(cur) > 2:
                cur[s[start]] -= 1
                if cur[s[start]] == 0:
                    del cur[s[start]]
                start += 1
            maxlen = max(maxlen, i-start + 1)
        return maxlen
                