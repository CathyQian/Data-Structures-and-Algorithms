"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""

# maintain a moving window, the left border is start and the right border is current index
# if duplicates found, move the start pointer to the last position of the detected duplicates.

class Solution:
    def lengthOfLongestSubstring(self, s):
        val_pos = {}
        res, start = 0, -1
        for i, c in enumerate(s):
            if c in val_pos and start < val_pos[c]:
                start = val_pos[c]
            res = max(res, i - start)
            val_pos[c] = i
        return res