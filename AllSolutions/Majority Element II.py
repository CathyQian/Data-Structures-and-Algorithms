"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]

Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]


"""

# Moore voting algorithm, similar to 169, the major difference is the last line for verification
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        v1 = [None, 0]
        v2 = [None, 0]
        for num in nums:
            if v1[1] == 0:
                v1 = [num, 1]
            elif v2[1] == 0:
                v2 = [num, 1]
            elif num == v1[0]:
                v1[1] += 1
            elif num == v2[0]:
                v2[1] += 1
            else:
                v1[1] -= 1
                v2[1] -= 1
        return [v for v in (v1[0], v2[0]) if nums.count(v) > len(nums)//3]
        