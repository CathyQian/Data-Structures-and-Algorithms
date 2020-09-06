"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
# dynamic programming
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for x in range(target + 1):
            for y in nums:
                if y > target:
                    break
                elif x + y <= target:
                    dp[x + y] += dp[x]
               
        return dp[target]

"""
Key point (method 2):DP

all numbers can be used any times
permutation instead of combination
DP:

state: dp[i] represents the number of permutations with sum equals to i
function: dp[i+j] += dp[i] for j in nums and i+j <= target
initialization: dp[0] = 1
results: dp[target]
"""


# DFS 
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort() # needed to terminate for loop earlier
        self.memo ={}
        return self.dfs(nums, target)
    
    def dfs(self, nums, target):
        ans = 0
        for num in nums:
            if target == num:
                ans = ans+1
            elif target > num:
                if target-num not in self.memo:
                   subans = self.dfs(nums, target-num)
                   self.memo[target-num] = subans
                ans += self.memo[target-num]
            else:# target < num
                return ans
        return ans
