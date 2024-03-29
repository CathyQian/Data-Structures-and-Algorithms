"""
Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

 

Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.


"""

# time complexity O(N), space complexity O(N)
# if using one dic, time complexity O(N2)
class Solution(object):
    def isIsomorphic(self, s, t):
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]: # one char map to multiple chars
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]: # multiple chars map to one char
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True