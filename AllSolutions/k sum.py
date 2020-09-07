"""
Description

Given n distinct positive integers, integer k (k <= n) and a number target.

Find k numbers where sum is target. Calculate how many solutions there are?
Have you met this question in a real interview?  
Example

Example 1

Input:
List = [1,2,3,4]
k = 2
target = 5
Output: 2
Explanation: 1 + 4 = 2 + 3 = 5

Example 2

Input:
List = [1,2,3,4,5]
k = 3
target = 6
Output: 1
Explanation: There is only one method. 1 + 2 + 3 = 6


"""

Lintcode hard

class Solution:
    def kSum(A: list, k: int, target: int) -> int:
        self.count = 0
        self.visited = set()
        self.dfs(range(1, n+1), k, target, 0, 0)
        return self.count
    def dfs(self, A, k, target, start, cursum):
        if k == 0 and cursum == target:
            self.count += 1
            return True
        for i in range(start, len(A)):
            if nums[i] not in self.visited:
                self.visited.add(A[i])
                if not self.dfs(A, k-1, target, i+1, cursum + A[i]):
                    self.visited.remove(nums[i])
        return False
        
           
