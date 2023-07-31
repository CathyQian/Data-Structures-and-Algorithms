"""
Word Pattern II

Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

 

Example 1:

Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
Example 2:

Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
Example 3:

Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false
 

Constraints:

1 <= pattern.length, s.length <= 20
pattern and s consist of only lowercase English letters.

"""

# DFS search with backtracking
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        # M is a dictionary has key-value: pattern:string
        # N is a dictionary has key-value: string:pattern
        # we can use M to find if a pattern has been matched
        # we can use N to find if a specific substring has been matched to a pattern
        M, N = {}, {}
        
        return self.search(pattern, s, M, N)
    def search(self, pattern, s, M, N):
        if len(pattern) == 0 and len(s) == 0:
            return True
        elif len(pattern) == 0 or len(s) == 0:
            return False
        else:
            if pattern[0] in M and s[: len(M[pattern[0]])] != M[pattern[0]]:
                return False
            elif pattern[0] in M and s[: len(M[pattern[0]])] == M[pattern[0]]:
                return self.search(pattern[1:], s[len(M[pattern[0]]):], M, N)
            else:
                for i in range(len(s)):
                    if s[: i + 1] not in N: # note M and N are not changed in this for loop
                        X = M | {pattern[0]: s[:i + 1]}
                        Y = N | {s[:i + 1]: pattern[0]}
                        if self.search(pattern[1:], s[i + 1:], X, Y):
                            return True
                        # standard backtracking code
                        # M.update({pattern[0]: s[:i + 1]})
                        # N.update({s[:i + 1]: pattern[0]})
                        # if self.search(pattern[1:], s[i+1:], X, Y):
                        #     return True
                        #else:
                        #    M.pop(pattern[0])
                        #    N.pop(s[:i+1])
                return False