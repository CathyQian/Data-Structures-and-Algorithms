"""
Maximum Profit in Job Scheduling

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:



Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104

"""

# dp, but time exceed limit; time complexity O(n2)
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # dp
        # state: dp[i]: max profit with ending time endTime[i]
        # relationship: dp[i] = max(dp[j] + profit between [startTime[j], endTime[i]] for j in) 
        # initialization: dp[i] = profit (basically only one task to start with)
        # result: max(dp[i])
        
        # sort time/profit with endTime, then scan from left to right
        timeProfit = list(zip(endTime, startTime, profit))
        timeProfit.sort()
        dp = [p for (_, _, p) in timeProfit]    
        for i in range(1, len(dp)):
            curendT, curstartT, p = timeProfit[i]
            for j in range(i): # these two lines are inefficient since needs to scan all < i indexex
                if timeProfit[j][0] <= curstartT:
                    dp[i] = max(dp[i], dp[j] + p)
        return max(dp)


# dp with binary search -- work but still not optimized
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort by end time
        timeProfit = list(zip(startTime, endTime, profit))
        timeProfit.sort(key=lambda x: x[1]) # sort by endTime
        # dp: 
        # state: dp[i] max profit at endtime[i]
        # relationship: for i in range(1, len(profit)):
        #                     dp[i] = max(dp[i-1], profit[i]) # not include; dp[i] = max(dp[j] + profit[i], dp[i-1]) # include if we can find j, scan back
        # initialization: dp[0] = endTime[0], else  -1
        # result: dp[-1]
        m = len(profit)
        dp = [0 for _ in range(m)]
        dp[0] = timeProfit[0][2]
        for i in range(1, len(profit)): # O(n)
            start_i, end_i, profit_i = timeProfit[i][0], timeProfit[i][1], timeProfit[i][2]
            # use binary search to find the largest end smaller or equal to start_i, return None if can't find
            j = self.jobSchedulingHelper(timeProfit, start_i) # O(logn)
            print(j)
            if j >= 0:
                dp[i] = max(dp[j] + profit_i, dp[i-1])
            else:
                dp[i] = max(profit_i, dp[i-1])
        return dp[-1]
    
    def jobSchedulingHelper(self, timeProfit, targettime):
        left, right = 0, len(timeProfit)
        while left <= right:
            mid = left + (right - left)//2
            if timeProfit[mid][1] <= targettime:
                left = mid + 1
            else:
                right = mid -1 
        return right
    
# dp with modification
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        timeProfit = list(zip(endTime, startTime, profit))
        timeProfit.sort()
        dp = [0] * len(timeProfit)  

        # calculate the first job can be picked up before ith job -- this makes code much faster
        prev = [-1] * len(dp)
        for i in range(1, len(dp)): # O(n2)
            for j in range(i-1, -1, -1):
                if timeProfit[j][0] <= timeProfit[i][1]:
                    prev[i] = j
                    break
        dp[0] = timeProfit[0][2]
        for i in range(1, len(dp)): # O(n)
            _, _, p = timeProfit[i]
            if prev[i] == '-1':
                dp[i] = max(dp[i-1], p)
            else:
                dp[i] = max(dp[i-1], dp[prev[i]] + p)
        return dp[-1]

# sorting + priority queue
from heapq import heappush, heappop

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        maxprofit = 0
        heap = []
        
        for start, end, profit in jobs:
            while heap and start >= heap[0][0]:
                maxprofit = max(maxprofit, heap[0][1])
                heappop(heap) # this line makes the code more efficient
            
            combined_job = (end, profit + maxprofit)
            
            heappush(heap, combined_job)
            
        while heap:
            maxprofit = max(maxprofit, heap[0][1])
            heappop(heap)
        
        return maxprofit