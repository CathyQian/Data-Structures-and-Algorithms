"""
Subarray Sums Divisible by K

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104

"""
# brutal force, TLE
# class Solution:
#     def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         if len(nums) == 0 or k == 0:
#             return 0
#         sumresidual = [0]
#         for i in range(len(nums)):
#             sumresidual.append(sumresidual[-1] + nums[i]%k)
#         cnt = 0
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 total = sumresidual[j+1] - sumresidual[i]
#                 if total%k == 0:
#                     cnt += 1
#         return cnt 


# time complexity: O(n+k); space complexity: O(k)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 or k == 0:
            return 0
        residual_idx = collections.defaultdict(list)
        sums = [0]
        for i in range(len(nums)): # O(n)
            sums.append(sums[-1] + nums[i])
            residual_idx[sums[-1]%k].append(i)
        cnt = 0
        for residual, idx_list in residual_idx.items(): # O(k)
            n = len(idx_list)
            cnt += n*(n-1)/2
            if residual == 0:               
                cnt += n
        return int(cnt) 