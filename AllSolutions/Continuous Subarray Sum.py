"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a
 continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is
  also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

 

Note:

    The length of the array won't exceed 10,000.
    You may assume the sum of all the numbers is in the range of a signed 32-bit integer.


"""
# method 1 Hash Table, to restore modulus or reminder, O(n)
from collections import defaultdict

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        sums = 0
        mods = collections.defaultdict(list)
        mods[0] = [-1]
        for i in range(len(nums)):
            sums += nums[i]
            if k: # k != 0
                mod = sums%k
                if mod in mods and i - mods[mod][0]> 1 :
                    return True
                else:
                    mods[mod].append(i)
            else: # k == 0
                if sums in mods and i-mods[sums][0]>1:
                    return True
                else:
                    mods[sums].append(i)
        return False
