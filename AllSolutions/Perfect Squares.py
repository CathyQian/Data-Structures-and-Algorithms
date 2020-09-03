"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which 
sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

# reference: https://yucoding.blogspot.com/2016/12/leetcode-question-perfect-square.html
# solution 1: BFS, key: put layer# in stack, remove visited so that the path is the shortest
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        visited = set()
        q = [(n, 0)]
        while q:
            ele, length = q.pop(0)
            k = 1
            while k*k <= ele:
                if ele == k*k:
                    return length + 1
                if ele-k*k not in visited:
                    visited.add(ele-k*k)
                    q.append((ele-k*k, length + 1))
                k += 1

# solution 2: DP, time complexity O(n^1.5), slower than BFS method
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            min_num = n
            j = 1
            while j*j <= i:
                min_num = min(dp[i-j*j] + 1, min_num)
                j += 1
            dp[i] = min_num
        return dp[n]