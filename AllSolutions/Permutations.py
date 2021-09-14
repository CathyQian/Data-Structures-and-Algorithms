"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""
# solution 1: dfs (preferred)
# time complexity: O(n*n!) n! permutations, n steps to calculate each permutation
# space complexity: O(n*n!)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, path):
        if len(nums) == 0:
            if path:
                res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], res, path + [nums[i]])

# solution 2: recursion, not as extendable as dfs
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        l = len(nums)
        if l <= 1:
            return [nums]
        
        temp = self.permute(nums[:-1])
       
        for i in range(len(temp)):
            for k in range(len(temp[i]) + 1):
                res.append(temp[i][:k] + [nums[l-1]] + temp[i][k+1:])
        return res
