"""
Find all possible combinations of k numbers that add up to a number n, given that
only numbers from 1 to 9 can be used and each combination should be a unique set
 of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution:
    def combinationSum3(self, k, n):
        res = []
        self.dfs(range(1,10), n, 0, [], res, k)
        return res

    def dfs(self, nums, target, index, path, res, k):
        if target < 0:
            return  # backtracking
        if target == 0 and len(path) == k:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(list(nums[:i]) + list(nums[i+1:]), target-nums[i], i, path + [nums[i]], res, k)    
