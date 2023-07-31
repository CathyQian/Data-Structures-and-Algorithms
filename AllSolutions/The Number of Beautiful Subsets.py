"""
The Number of Beautiful Subsets

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].
 

Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000


"""

# Combination via DFS

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        if not nums: 
            return 0
        if len(nums) == 1: 
            return 1
        self.res = 0
        self.dfs(nums, 0, [], k, set())
        return self.res
    
    def dfs(self, nums, start, path, k, forbidden):
        if path:
            self.res += 1
        for i in range(start, len(nums)):
            if nums[i] not in forbidden:
                self.dfs(nums, i+1, path + [nums[i]], k, forbidden|{nums[i]+k, nums[i]-k})

