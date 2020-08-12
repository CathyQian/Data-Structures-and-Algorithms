"""
Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Follow up: Your solution should be in logarithmic complexity.

"""
# time complexity: O(n)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0: 
                if len(nums) > 1 and nums[0] > nums[1] or len(nums) == 1: # edge case len(nums) == 1
                    return 0
            elif i == len(nums)-1 and i-1 >= 0 and nums[i] > nums[i-1]:
                return len(nums) - 1
            elif i-1 >= 0 and i+1 < len(nums) and nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        return -1

# similar as the previous solution, but simplified by adding heading and trailing elements
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float('-inf'))
        nums.insert(0, float('-inf'))

        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i-1
                
        return -1
    
# binary search, time complexity: O(logN)
# tricky:
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r -l ) // 2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l
