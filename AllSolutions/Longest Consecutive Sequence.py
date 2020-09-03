"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxlen = 0
        for num in nums:
            if num - 1 not in nums_set:
                curlen = 1
                while num + 1 in nums_set:
                    curlen += 1
                    num += 1
                maxlen = max(maxlen, curlen)
        return maxlen