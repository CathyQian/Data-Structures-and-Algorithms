"""
Given an integer array with all positive numbers and no duplicates, find the
 number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
"""和之前的区别是：不要求连续array, 但是all positive numbers and no duplicates,
positive integer target

解题思想有点像之前爬梯子的那道题Climbing Stairs，我们需要一个一维数组dp，其中dp[i]表示
目标数为i的解的个数，然后我们从1遍历到target，对于每一个数 x+y，遍历nums数组 y，如果 x+y < target,
dp[x+y] += dp[x]。这个也很好理解，比如说对于[1,2,3] 4，这个例子，当我们在计算dp[3]
的时候，3可以拆分为1+x，3也可以拆分为2+x，3同样可以拆为3+x，此时x为dp[0]，我们把所有的情况加起来就是组成3的所有情况

类似题目: combination sum, 不同的是要return solutions set, 而本题是要回复number of solutions
回复number用dp, 回复所有solution set用枚举 (dfs or bfs)
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for x in range(target + 1):
            for y in nums:
                if x + y <= target:
                    dp[x + y] += dp[x]
        return dp[target]
