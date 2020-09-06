"""Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the
total number of rows in the triangle.
"""

"""
Since this problem aims to find the minimum path from top to bottom, so all possible path
should be considered. We can go through brutal force by checking every possible path but 
that is quite time consuming. Alternatively, we can use dynamic programming from bottom to top.
state dp[j]: minimum sum from bottom to current layer, at jth node from left to right
initialization: dp = triangle[-1]
function: dp[j] = triangle[i][j] + min(dp[j], [j+1])
result: dp[0]
"""

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]

        return dp[0]
