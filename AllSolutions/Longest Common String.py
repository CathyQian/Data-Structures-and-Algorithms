"""
Given two strings, find the longest common substring.
Return the length of it.
"""

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        maxlength = len(A) + 1
        for i in range(maxlength)[::-1]:
            substrB = []
            for j in range(len(B) + 1 - i):
                substrB.append(B[j: j + i])
            for str in substrB:
                if A.find(str) != -1:
                    return i
        return 0