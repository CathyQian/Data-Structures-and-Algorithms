"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

 

Constraints:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


"""

# method 1, brutal force
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sums = nums[i]
            for j in range(i, len(nums)):
                if j > i:
                    sums += nums[j]
                if sums == k:
                    count += 1
        return count

# method 2
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, cumsum = 0, 0
        lookup = collections.defaultdict(int) # default value all 0
        lookup[0] = 1
        for num in nums:
            cumsum += num
            res += lookup[cumsum-k]
            lookup[cumsum] += 1
        return res