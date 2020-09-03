"""
Given an integer array, adjust each integers so that the difference of every adjacent integers are not greater than a given number target.

If the array before adjustment is A, the array after adjustment is B, you should minimize the sum of |A[i]-B[i]|

You can assume each number in the array is a positive integer and not greater than 100.
Have you met this question in a real interview?  
Example

Example 1:
	Input:  [1,4,2,3], target=1
	Output:  2

Example 2:
	Input:  [3,5,4,7], target=2
	Output:  1
	

Related Problems
"""

"""
Time complexity: O(100*target*n)

Space complexity: O(n)


这是一个背包问题，不太容易看出来。因为数的范围是1~100，每个数有100中调整的可能性，采用动态规划的思路。
建立大小为(n+1)*101的数组dp记录所有可能调整的代价，初始化为全0.
dp中第i个iteration对应加入A[i-1]。对于每个数A[i]，调整后的结果有100种，用dp[j]表示数字A[i]调整为j的最小代价。
对于每个dp[j]，A[i-1]调整到k的代价加上A[i]调整到j的最小代价即为dp[j]的代价。而k又有100种选择，对于j，
当|j-k|的绝对值不大于target时，代价最小，rec[j]保留所有可能代价中的最小代价。iteration完了返回min(rec[j]).
"""

class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        maxNum = 100
        pre_dp = [0]*(maxNum+1)
        
        for i in range(len(A)):
            post_dp = [None]*(maxNum+1)
            for cur in range(0, maxNum+1):
                post_dp[cur] = min([pre_dp[pre] + abs(cur -A[i]) for pre in range(0, maxNum+1) if abs(pre-cur) <= target])
            pre_dp = post_dp
            
        return min(post_dp)