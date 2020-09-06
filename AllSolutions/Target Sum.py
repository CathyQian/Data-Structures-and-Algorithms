"""
Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, 
you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

 

Constraints:

    The length of the given array is positive and will not exceed 20.
    The sum of elements in the given array will not exceed 1000.
    Your output answer is guaranteed to be fitted in a 32-bit integer.


"""

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = dict()
        return self.dfs(nums, S, 0, memo)
        
    def dfs(self, nums, s, start, memo):
        if (start, s) not in memo:
            result = 0
            if start == len(nums):
                if s == 0:
                    result += 1
            else:
                result += self.dfs(nums, s-nums[start], start+1, memo)
                result += self.dfs(nums, s+nums[start], start+1, memo)
            memo[(start, s)] = result
        return memo[(start,s)]
