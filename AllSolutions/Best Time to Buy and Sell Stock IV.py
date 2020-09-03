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
# state machine
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

# method 2, dp
class Solution:
    def maxProfit(self, k, prices):
        if not prices:
            return 0
        
        if k >= len(prices)//2:
            profit = 0
            for i in range(1, len(prices)):
                diff = prices[i]-prices[i-1]
                if diff > 0:
                    profit += diff
            return profit
        
        l, g = [0] * (k+1), [0] * (k+1)
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k+1)[::-1]: # 1D dp to save space, scan j reversed
                l[j] = max(g[j - 1] + max(diff, 0), l[j] + diff)
                g[j] = max(g[j], l[j])
                
        return g[-1]       
