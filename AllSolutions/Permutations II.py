"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, path):
        if len(nums) == 0:
            if path:
                res.append(path)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                self.dfs(nums[:i] + nums[i+1:], res, path + [nums[i]])