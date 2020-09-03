"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""
# DP, too slow though
#state: f[i]: whether nums[i] is accesbile, true or false
# function: if f[j] and i - j <= nums[j]: f[i] = true
# initialize: f[0]= True, all others false
# result: f[-1]
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        f = [False for i in range(length)]
        f[0] = True
        for i in range(1, length):
            for j in range(0, i):
                if f[j] and i - j <= nums[j]:
                    f[i] = True
        return f[-1]

# no DP, m is the maximum achievable point at i index
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
