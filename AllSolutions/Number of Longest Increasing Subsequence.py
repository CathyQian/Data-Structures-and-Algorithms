"""
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:

Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int. 
"""
# DP solution ref: https://www.cnblogs.com/grandyang/p/7603903.html
# len[i] 表示以 nums[i] 为结尾的递推序列的长度，用 cnt[i] 表示以 nums[i] 为结尾的max length递推序列的个数，初始化都赋值为1，只要有数字，那么至少都是1
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length, cnt = [1]*len(nums), [1]*len(nums)
        mx, res = 0, 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j] + 1:
                        cnt[i] += cnt[j]
                    elif length[i] < length[j] + 1:
                        length[i] = length[j]+1
                        cnt[i] = cnt[j]
            if mx == length[i]:
                res += cnt[i]
            elif mx < length[i]:
                mx = length[i]
                res = cnt[i]
        return res
