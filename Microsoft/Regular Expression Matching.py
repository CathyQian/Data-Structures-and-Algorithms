"""
Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

"""

"""
- both s and p needs to be fully matched without residual
- * here can also remove the preceding element, which is different from 'Wildcard Matching'
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
       
        if len(p) == 0:
            return len(s) == 0
        
        if len(p) == 1:
            return (len(s) == 1 and (s[0]==p[0] or p[0]=='.'))
        
        # len(p) > 1
        if p[1] != '*':
            if len(s) == 0:
                return False
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        
        # len(p) > 1 and p[1] == '*' and first letter match with s
        while len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):# * stands for repeating once
                return True
            s = s[1:]
        # len(p) > 1 and p[1] != '*' and first letter doesn't match with s, * stands for repeating zero times
        return self.isMatch(s, p[2:])