"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

# recursion:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        res = self.subsets(nums[:-1])
        return res + [i+[nums[-1]] for i in res]
                
        
# for loop
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for i in range(len(nums)):
            for j in range(len(res)):
                res.append(res[j] + [nums[i]])
                
        return res
            
        
            
# dfs, retrieval order is different from previous two methods: [], [1], [1,2], [1,2,3], [2], [2,3]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, start, path, res):
        res.append(path)
        for i in range(start, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res) # 类似于graph, 每个数能reach到它后面的数，形成一条path
        return
    
