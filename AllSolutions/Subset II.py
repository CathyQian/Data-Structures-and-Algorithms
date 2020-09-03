"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
"""
拿题目中的例子 [1 2 2] 来分析，根据之前 Subsets 里的分析可知，当处理到第一个2时，此时的子集合为 [], [1], [2], [1, 2]，
而这时再处理第二个2时，如果在 [] 和 [1] 后直接加2会产生重复，所以只能在上一个循环生成的后两个子集合后面加2，发现了这一点，
题目就可以做了，我们用 last 来记录上一个处理的数字，然后判定当前的数字和上面的是否相同，若不同，则循环还是从0到当前子集的
个数，
若相同，则新子集个数减去之前循环时子集的个数当做起点来循环，这样就不会产生重复
"""
# for loop
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(res)
            for j in range(len(res)-l, len(res)):
                res.append(res[j] + [nums[i]])
        return res

# dfs
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.dfs(result, [], nums, 0)
        return result
    
    def dfs(self, result, base, nums, start):
        result.append(base)
        curr = -sys.maxsize # why not in for loop?  nums[idx] == nums[idx-1]
        for idx in range(start, len(nums)):
            if nums[idx] == curr:
                continue
            else:
                self.dfs(result, base+[nums[idx]], nums, idx+1)
                curr = nums[idx]
        return

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()                      
        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, start, path, result):
        result.append(path)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], result)
        return