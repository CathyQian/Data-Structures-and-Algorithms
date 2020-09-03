"""
You are given a string s containing lowercase letters and an integer k. You need to :

    First, change some characters of s to other lowercase English letters.
    Then divide s into k non-empty disjoint substrings such that each substring is palindrome.

Return the minimal number of characters that you need to change to divide the string.

 

Example 1:

Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.

Example 2:

Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.

Example 3:

Input: s = "leetcode", k = 8
Output: 0

 

Constraints:

    1 <= k <= s.length <= 100.
    s only contains lowercase English letters.

Accepted
6,721
Submissions
11,382
"""

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        dp = [[0 for _ in range(k)] for _ in range(len(s))]
        for i in range(1, len(s)):
            for j in range(k):
                if j == 0:
                    dp[i][j] = self.num_count(s, 0, i)
                elif j < i:
                    dp[i][j] = min(dp[m][j-1] + self.num_count(s, m+1, i) for m in range(j-1, i))
        return dp[len(s)-1][k-1]
    
    def num_count(self, s, start, end):
        count = 0
        while start <= end:
            if s[start] != s[end]:
                count += 1
            start += 1
            end -= 1
        return count


"""dp
"""