"""
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


"""
# state machine (hard to understand)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if k >= n/2:
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
        buy = [-sys.maxsize] * (k+1)
        sell = [0] * (k+1)
        for i in range(len(prices)):
            pre_buy, pre_sell = buy.copy(), sell.copy()
            for j in range(1, k+1):
                buy[j] = max(pre_buy[j], pre_sell[j-1]-prices[i])
                sell[j] = max(pre_sell[j], pre_buy[j]+prices[i])
        return sell[-1]

# method 2, dp (preferred)
"""
ref: https://www.cnblogs.com/grandyang/p/4295761.html
我们定义local[i][j]为在到达第i天时最多可进行j次交易并且最后一次交易在最后一天卖出的最大利润，此为局部最优。然后我们定义global[i][j]为在到达第i天时最多可进行j次交易的最大利润，此为全局最优。
它们的递推式为：
local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff) # local[i-1][j] not local[i-1][j-1], sale at (i-1)th day vs sale at ith day, while number of 
transactions doesn't change.
global[i][j] = max(local[i][j], global[i - 1][j])，
其中局部最优值是比较前一天并少交易一次的全局最优加上大于0的差值，和前一天的局部最优加上差值后相比，两者之中取较大值，而全局最优比较局部最优和前一天的全局最优。

change 2D array into 1D array, if j grow incrementally, l and g with smaller j will be updated first, so we still need 2D array. Therefore, j needs to decrease gradually, so 
we can still use 1D array to save some space.
"""
class Solution:
    def maxProfit(self, k, prices):
        if not prices:
            return 0
          
        # Can buy and sell anytime, no constraints
        if k >= len(prices)//2:
            profit = 0
            for i in range(1, len(prices)):
                diff = prices[i]-prices[i-1]
                if diff > 0:
                    profit += diff
            return profit
        
        l, g = [0] * (k+1), [0] * (k+1) # local and global max profit at the ith transactions (i from 1 to k)
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k+1)[::-1]: # 1D dp to save space, scan j reversed
                l[j] = max(g[j - 1] + max(diff, 0), l[j] + diff)
                g[j] = max(g[j], l[j])
                
        return g[-1]       
