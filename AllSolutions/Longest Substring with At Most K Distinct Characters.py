"""
Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.


"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        cur = collections.defaultdict(int)
        maxlen = 0
        start = 0
        for i, ss in enumerate(s):
            cur[ss] += 1
            while len(cur) > k:
                cur[s[start]] -= 1
                if cur[s[start]] == 0:
                    del cur[s[start]]
                start += 1
            maxlen = max(maxlen, i-start + 1)
        return maxlen