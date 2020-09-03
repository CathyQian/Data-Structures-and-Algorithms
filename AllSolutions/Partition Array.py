"""
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

    All elements < k are moved to the left
    All elements >= k are moved to the right

Return the partitioning index, i.e the first index i nums[i] >= k.

You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length

Example 1:

Input:
[],9
Output:
0

Example 2:

Input:
[3,2,2,1],2
Output:1
Explanation:
the real array is[1,2,2,3].So return 1

Challenge

Can you partition the array in-place and in O(n)?

"""
class Solution:
    def partition(self, nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] < k:
                nums[i], nums[count] = nums[count], nums[i]
                count += 1
        return count

