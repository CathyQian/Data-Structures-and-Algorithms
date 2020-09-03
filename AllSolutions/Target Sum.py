class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = dict()
        return self.dfs(nums, S, 0, memo)
        
    def dfs(self, nums, s, start, memo):
        if (start, s) not in memo:
            result = 0
            if start == len(nums):
                if s == 0:
                    result += 1
            else:
                result += self.dfs(nums, s-nums[start], start+1, memo)
                result += self.dfs(nums, s+nums[start], start+1, memo)
            memo[(start, s)] = result
        return memo[(start,s)]