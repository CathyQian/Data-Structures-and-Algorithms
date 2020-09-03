"""
Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""
# right solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]: # tell if mid and start are in the same branch, only one senario
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else: # nums[mid] < nums[start]:
                if target <= nums[end] and nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

# wrong solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:# there can be multiple senarios
                if target >= nums[start] and nums[start] <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else: # nums[mid] < target:
                if target <= nums[end] and nums[mid] < nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1