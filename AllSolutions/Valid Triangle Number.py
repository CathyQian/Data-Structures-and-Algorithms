"""
Valid Triangle Number

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:

Input: nums = [4,2,3,4]
Output: 4

 

Constraints:

    1 <= nums.length <= 1000
    0 <= nums[i] <= 1000


"""

# brutal force is O(n3)
# optimized solution is O(n2)
class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        count, n =  0, len(nums)
        for i in range(2, n):
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
        return count