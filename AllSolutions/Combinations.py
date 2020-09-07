"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution:
    def combine(self, n,k):
        result = []
        self.combineDFS(n, 0, [], k, result)
        return result

    def combineDFS(self, n, start, path, k, result):
        if k == 0:
            result.append(path)
            return
        for i in range(start, n):
            self.combineDFS(n, i+1, path+[i+1], k-1, result)
