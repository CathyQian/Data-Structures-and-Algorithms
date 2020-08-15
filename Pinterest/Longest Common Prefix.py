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
        res, m = "", len(strs)
        if m == 0: # edge case, or else min() will have no inputs
            return res
        j = 0
        minlength = min([len(strs[i]) for i in range(m)])
        while j < minlength:
            val = strs[0][j]
            for i in range(1, m):
                if strs[i][j] != val:
                       return res
            res += val
            j += 1
        return res
            