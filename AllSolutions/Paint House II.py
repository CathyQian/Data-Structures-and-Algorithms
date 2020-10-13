"""
Paint House II

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the 
houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2]
is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 

Follow up:
Could you solve it in O(nk) runtime?

"""
# dynamic programming, from top to bottom, O(nk^2) runtime, space: O(k)

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        n, k = len(costs), len(costs[0])
        dp = [[0 for _ in range(k)] for _ in range(n)]
        
        dp[0] = costs[0]
        for i in range(1, n):
            for j in range(k):
                dp[i][j] = costs[i][j] + min(dp[i-1][l] for l in range(k) if l != j)
        return min(dp[n-1])

# similar, space O(k)    

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        n, k = len(costs), len(costs[0])
        
        
        pre = costs[0]
        for i in range(1, n):
            cur = [0]*k # remember to initialize at each round, or else it will point and modify pre
            for j in range(k):
                cur[j] = costs[i][j] + min(pre[l] for l in range(k) if l != j)
            pre = cur
        return min(pre)

# method 3, DP, optimize based on the second solution, time O(nk), space O(k)

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        n, k = len(costs), len(costs[0])
        pre = costs[0]
        for i in range(1, n):
            cur = [0]*k
            premin = self.min2(pre)  # O(k)
            for j in range(k):  # O(k)
                cur[j] = costs[i][j] + premin[j]
            pre = cur
        return min(pre)
    
    def min2(self, pre):
        minimum = sys.maxsize
        min1 = min(pre)
        minidx = pre.index(min1)
        min2 = min(pre[:minidx] + pre[minidx+1:])
        res = [0] * len(pre)
        for i in range(len(pre)):
            if i == minidx:
                res[i] = min2
            else:
                res[i] = min1
        return res
        
