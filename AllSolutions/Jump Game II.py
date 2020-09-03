"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:

You can assume that you can always reach the last index.

"""
# method 1, dp, time exceed limit
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            dp[i] = min([dp[j] + 1 for j in range(i)[::-1] if j + nums[j]>=i]) 
        return dp[-1]

class Solution:
    def jump(self, nums: List[int]) -> int:
        f = [0 for _ in range(len(nums))]
    
        for i in range(1, len(nums)):
            minSteps = len(nums) + 1
            for k in range(i)[::-1]:
                if nums[k] >= i - k:
                    minSteps = min(minSteps, f[k] + 1)
            f[i] = minSteps
        return f[-1]

# method 2
"""
Idea for method 2:
- The idea is to maintain two pointers left and right, where left initialy set to be 0 and right set to be nums[0].
- So points between 0 and nums[0] are the ones you can reach by using just 1 jump.
- Next, we want to find points I can reach using 2 jumps, so our new left will be set equal to right, and our new right will be set equal to the farest point we can reach by two jumps. which is:
right = max(i + nums[i] for i in range(left, right + 1)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return 0
        l, r = 0, nums[0]
        steps = 1
        while r < len(nums) - 1:
            steps += 1
            max_r = max([i + nums[i] for i in range(l, r+1)])
            l, r = r, max_r
        return steps