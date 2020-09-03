# -*- coding: utf-8 -*-
"""
Given an array S of n integers, are there elements a, b, c, and d in S such
that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is: [ [-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2] ]
"""
"""重点：排序，然后从两头开始扫，跳过重复元素
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums, result = sorted(nums), []
        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i - 1]: #跳过重复元素
                continue
            for j in reversed(range(i + 3, len(nums))):
                if j != len(nums) - 1 and nums[j] == nums[j + 1]: #跳过重复元素
                    j -= 1
                    continue
                k, m = i + 1, j - 1 #确定首尾后扫描中间的元素
                while k < m:
                    temp = nums[i] + nums[j] + nums[k] + nums[m]
                    if temp < target:
                        k += 1
                    elif temp > target:
                        m -= 1
                    else:
                        if [nums[i], nums[j], nums[k], nums[m]] not in result:
                            result.append([nums[i], nums[j], nums[k], nums[m]])
                        k += 1
                        m -= 1
                        # 继续跳过重复元素
                        while k < m and nums[k] == nums[k - 1]:
                            k += 1
                        while k < m and nums[m] == nums[m + 1]:
                            m -= 1

        return result
