"""
[Leetcode](https://leetcode.com/problems/trapping-rain-water/)

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        left, right = [0]*n, [0]*n
        left[0] = height[0]
        right[-1] = height[-1]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i]) # no need to get curmax
        for j in range(0, n-1)[::-1]:
            right[j] = max(right[j+1], height[j])
            
        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - height[i]
        return water