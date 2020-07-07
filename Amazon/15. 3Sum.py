"""
[Leetcode](https://leetcode.com/problems/3sum/)

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
        for i in range(len(nums)-2):
            if i == 0 or i > 0 and nums[i] != nums[i-1]: # needed to remove duplicates
                j, k = i+1, len(nums) - 1
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    if s == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        # remove duplicates, key
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1
                    elif s > 0:
                        k -= 1
                    else:
                        j += 1
        return res