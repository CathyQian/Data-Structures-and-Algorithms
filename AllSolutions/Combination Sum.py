"""
类似题目:
1) combination sum IV, 不同的是要return solutions set
回复number用dp, 回复所有solution set用枚举 (dfs or bfs)
2) Combination 要回复所有solution set用dfs枚举
"""
"""
Given a set of candidate numbers (candidates) (without duplicates) and a target
 number (target), find all unique combinations in candidates where the candidate
 numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
# dfs
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(sorted(candidates), result, 0, [], target)
        return result

    def dfs(self, candidates, result, start, path, target):
        if target == 0 and path:
            result.append(path)
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                else:
                    self.dfs(candidates, result, i, path + [candidates[i]], target - candidates[i])


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # combination instead of permutation since the number order returned doesn't matter
        # all integers are distinct, so no need to worry about redundant answers in results
        # all intergers are positive, so sort the candidates can allow early interruption of loop
        # each number can be used an unlimited number of times
        candidates.sort() # allow early interruption of DFS loop to make the code run faster
        self.res = []
        self.dfs(candidates, target, 0, 0, [])
        return self.res
    def dfs(self, candidates, target, start, cursum, path):
        if cursum == target and path:
            self.res.append(path)
        else:
            for i in range(start, len(candidates)):
                if candidates[i] + cursum > target:
                    break
                else:
                    self.dfs(candidates, target, i, cursum + candidates[i], path + [candidates[i]])
        return