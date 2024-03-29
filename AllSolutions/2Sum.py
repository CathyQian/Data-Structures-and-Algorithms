"""
[Leetcode link](https://leetcode.com/problems/two-sum/)

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        residual = {}
        for i, num in enumerate(nums):
            if num in residual:
                return [residual[num], i]
            else:
                residual[target-num] = i
                
# If there's duplicated elements, return all possible pairs
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {} # ele: [idx,idx,...] residual also works
        res = []
        for i in range(len(nums)):
            if target - nums[i] in visited:
                res.extend([[k, i] for k in visited[target-nums[i]]])
            else:
                if nums[i] in visited:
                    visited[nums[i]].append(i)
                else:
                     visited[nums[i]] = [i]
