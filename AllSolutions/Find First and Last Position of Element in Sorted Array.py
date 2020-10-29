"""
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?


Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
"""

class Solution:
    def searchRange(self, nums, target):
        l = self.findLeft(nums, target)
        r = self.findRight(nums, target)
        return [l, r] if l <= r else [-1, -1]
    
    def findLeft(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l   
        
    def findRight(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r