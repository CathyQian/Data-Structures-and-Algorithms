"""
Longest Happy Prefix

A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s. Return the longest happy prefix of s .

Return an empty string if no such prefix exists.

 

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".

Example 2:

Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.

Example 3:

Input: s = "leetcodeleet"
Output: "leet"

Example 4:

Input: s = "a"
Output: ""

 

Constraints:

    1 <= s.length <= 10^5
    s contains only lowercase English letters.

"""

# method1: brutal force, O(n2)
class Solution:
    def longestPrefix(self, s: str) -> str:
        res = ''
        i, j = 0, len(s) - 1
        while i < len(s)-1:
            if s[:i+1] == s[j:]:
                res = s[:i+1]
            i += 1
            j -= 1
        return res
    
# brutal force, O(n2)
class Solution:
    def longestPrefix(self, s: str) -> str:
        longest = ''
        n = len(s)
        for i in range(n-1):
            if s[i] == s[n-1] and s[0] == s[n-1-i]:
                print(i)
                if s[:i+1] == s[n-1-i:]:
                    longest = s[:i+1]
        return longest
            
# method2: KMP algorithm: https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
class Solution:
    def longestPrefix(self, t: str) -> str:
        i, j, lps = 1, 0, [0]*len(t)
        while i < len(t):
            if t[i] == t[j]:
                j, lps[i] = j + 1, j + 1
                i += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        return t[:lps[-1]]
