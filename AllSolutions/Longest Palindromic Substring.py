"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"


"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, pal1, pal2 = "", "", ""
        
        for i in range(len(s)):
            pal1 = self.searchPalindrome(s, i, i)
            if i + 1 < len(s):
                pal2 = self.searchPalindrome(s, i, i+1)     
                
            if len(pal1) > len(res):
                res = pal1
            if len(pal2) > len(res): # not elif
                res = pal2
        return res
    
    def searchPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]