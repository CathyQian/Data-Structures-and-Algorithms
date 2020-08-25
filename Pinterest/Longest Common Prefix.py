"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: # edge case, or else min() will have no inputs
            return ""
        shortest = min(strs, key=len) # find shortest string
        for i, ch in enumerate(shortest):
            for others in strs:
                if others[i] != ch:
                    return shortest[:i]
        return shortest
            