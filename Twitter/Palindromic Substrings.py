"""
Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

 

Note:

    The input string length won't exceed 1000.

"""
# brutal force, time complexity O(n3)
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    count += 1
        return count

# use dp to figure out if dp[i: j] is palindromic or not first
# time complexity O(n2)

dp = [[False]*(n+1) for _ in range(n+1)]
# initialization:
i = 0, j = 0 True
i == j, True
return dp[0][n]

# relationship:
for i in range(n)[::-1]:
    for j in range(i, n):
        if nums