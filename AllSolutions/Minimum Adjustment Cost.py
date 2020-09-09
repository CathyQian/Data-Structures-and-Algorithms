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
dp[i][v]: the value of the ith element in A is modified to v, the min cost
i range from 0 to len(A) -1, V range from 0 to 100
2D dp can be replaced by 1D dp using pre and post array
"""

class Solution:
    def MinAdjustmentCost(self, A, target):
        maxNum = 100
        pre_dp = [0]*(maxNum+1)
        
        for i in range(len(A)):
            post_dp = [None]*(maxNum+1)
            for cur in range(0, maxNum+1):
                post_dp[cur] = min([pre_dp[pre] + abs(cur -A[i]) for pre in range(0, maxNum+1) if abs(pre-cur) <= target])
            pre_dp = post_dp
            
        return min(post_dp)
