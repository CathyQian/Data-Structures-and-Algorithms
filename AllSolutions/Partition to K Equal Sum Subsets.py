"""
Partition to K Equal Sum Subsets

Given an array of integers nums and a positive integer k, find whether it's possible to divide 
this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Note:

    1 <= k <= len(nums) <= 16.
    0 < nums[i] < 10000.

"""

"""
dfs
The key point here is that the nums list needs to be sorted in descending order before doing dfs. This is
because the search is more efficient starting from big numbers than small numbers.
Let's look at an example:
nums = [4,5,3,2,5,5,5,1,5,5,5,5,3,5,5,2]
k = 13

Sort nums in ascending order:
[1,2,2,3,3,4,5,5,5,5,5,5,5,5,5,5]

Target value = 5, if search from small value, [1,2,2] is one combination. However, this will leave the rest 
numbers impossible to divide into 12 groups with equal sum since big numbers are less flexible than small numbers.
This will result in Time Exceed Limit in OJ. 
If we search from the big numbers, we can quickly find all the 5, then 4 (find its match 1), then 3 (find its match 2)
Finished.
"""
# this is the most important line
# search is more efficient if start from bigger number compared to small number
# dfs
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False

        if sum(nums) % k != 0:
            return False
       
        nums.sort(reverse=True) # needs to be reversed !!!!!
        self.visited = [False] * len(nums) # record which numbers has been used so far
        self.target = sum(nums) // k
  
        return self.dfs(0, k, nums, self.target)

    def dfs(self, start, k, nums, target): # note consider all senarios in dfs, not the main function

        if k == 1: # k won't go to 0
            return True
        if target < 0: # only correct if all elements in nums are non-negative (Leetcode all test case yes!)
            return False
        if target == 0:   
            return self.dfs(0, k-1, nums, self.target)
        
        # core part
        for i in range(start, len(nums)): # exhaustive search
            if not self.visited[i]: # this node can't be used in the following dfs
                self.visited[i] = True
                if self.dfs(i+1, k, nums, target-nums[i]): #only need one True to return True
                    return True
                self.visited[i] = False # didn't find a path, reuse this node to try another route
            
        return False
