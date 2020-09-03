"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)-2):
            if k == 0 or nums[k] != nums[k-1]:
                i, j = k + 1, len(nums) - 1
                while i < j:
                    s = nums[k] + nums[i] + nums[j]
                    if s < 0: # skip duplicated elements here is optional
                        i += 1  
                    elif s > 0: # skip duplicated elements here is optional
                        j -= 1
                    else: # s = 0
                        res.append([nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i-1]:
                            i += 1
                        while i < j and nums[j] == nums[j+1]:
                            j -= 1
        return res