"""
Find Minimum in Rotated Sorted Array I, II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array doesn't contain duplicates (I)
The array may contain duplicates (II).

Example 1:

Input: [1,3,5]
Output: 1

Example 2:

Input: [2,2,2,0,1]
Output: 0

Note:

    This is a follow up problem to Find Minimum in Rotated Sorted Array.
    Would allow duplicates affect the run-time complexity? How and why?


"""
# I, array no duplicates, time complexity O(logn), space complexity O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums) - 1
        while start+1 < end: 
            mid = start + (end - start)//2
            if nums[mid] > nums[start] and nums[mid] < nums[end]:
                return nums[start]
            elif nums[mid] > nums[start] and nums[start] > nums[end]:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])
                
# II, array with duplicates, time complexity O(n), space complexity O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums) - 1
        while start+1 < end: 
            mid = start + (end - start)//2
            if nums[mid] == nums[start]: # add when duplicates allowed
                start += 1
            elif nums[mid] > nums[start] and nums[mid] <= nums[end]:
                return nums[start]
            elif nums[mid] > nums[start] and nums[start] >= nums[end]:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])
                