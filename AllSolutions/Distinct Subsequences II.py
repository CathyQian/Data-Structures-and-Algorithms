"""
Given a string S, count the number of distinct, non-empty subsequences of S .
Since the result may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:

Input: "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".

Example 3:

Input: "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

Note:

    S contains only lowercase letters.
    1 <= S.length <= 2000
"""

class Solution:
    def distinctSubseqII(self, S: str) -> int:
        dp = [1]*(len(S)+1)
        last = {}
        
        for i in range(1, len(S)+1):
            letter = S[i-1]
            dp[i] = 2*dp[i-1]
            if letter in last:
                dp[i] -= dp[last[letter]-1] #this part has been counted into dp[last[letter]] and dp[i-1]
            last[letter] = i
        return (dp[-1]-1)% (10**9 + 7)