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
        n = len(nums)
        sums = nums[:]
        for i in range(1,n):
            sums[i] += sums[i-1]
        
        mods = defaultdict(list)
        mods[0] = [-1] # corner case, when there is no element we have modulus as zero/when k = 0, the first 0 in sums appear, return True
        for idx, s in enumerate(sums):
            if k: # k != 0
                mod = s%k
                if mod in mods and idx - mods[mod][0]> 1 :
                    return True
                else:
                    mods[mod].append(idx)
            else: # k == 0
                if s in mods and idx-mods[s][0]>1:
                    return True
                else:
                    mods[s].append(idx)
        return False

# method 2: brutal force, O(n2)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            sums = nums[i]
            for j in range(i+1, len(nums)):
                sums += nums[j]
                if (k != 0 and sums%k == 0) or (sums == 0 and k == 0):
                    return True            
        return False