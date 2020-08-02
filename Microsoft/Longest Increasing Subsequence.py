"""
Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

"""
# method 1, dynamic programming, time complexity O(n2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """dynamic programming:
        dp[i]: longest xxx ending in nums[i], initialized to be 1 for all
        df[i] = max(dp[i], dp[j]+1)
        """
        if len(nums) == 0:
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
        return max(dp)

# binary search, time complexity O(nlogn)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if len(res) == 0 or len(res) > 0 and num > res[-1]:
                res.append(num)
            elif num < res[-1]:
                idx = self.insert(res, num)
                res[idx] = num
        
        return len(res)
    
    def insert(self, l: List[int], target: int) -> int:
        # find the index of first element in l >= target 
        start, end = 0, len(l) -1 
        while start <= end:
            mid = start + (end - start)//2
            if l[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        return start