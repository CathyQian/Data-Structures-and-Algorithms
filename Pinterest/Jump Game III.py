"""
Jump Game III

Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index 
with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3

Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.

Constraints:

    1 <= arr.length <= 5 * 10^4
    0 <= arr[i] < arr.length
    0 <= start < arr.length

"""

# method 1, dfs solution, find any zero
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.bool = False
        if len(arr) > start >= 0:
            self.dfs(arr, start, set())
        return self.bool
    
    def dfs(self, arr, start, visited):
        if self.bool:
            return 
        if arr[start] == 0:
            self.bool = True
            return
        else:
            visited.add(start)
            if len(visited) == len(arr):
                return
            if start + arr[start] < len(arr) and start + arr[start] not in visited:
                self.dfs(arr, start + arr[start], visited)
            if start - arr[start] >= 0 and start - arr[start] not in visited: # not elif
                self.dfs(arr, start - arr[start], visited)
            
# method 1, dfs, another way to write the code (I like it better)
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if len(arr) > start >= 0:
            return self.dfs(arr, start, set())
        return False
    
    def dfs(self, arr, start, visited):
        if arr[start] == 0:
            return True
        else:
            visited.add(start)
            if len(visited) == len(arr):
                return False
            if start + arr[start] < len(arr) and start + arr[start] not in visited:
                if self.dfs(arr, start + arr[start], visited):
                    return True
            if start - arr[start] >= 0 and start - arr[start] not in visited: # not elif
                if self.dfs(arr, start - arr[start], visited):
                    return True
            return False
            
# method 2, dfs, find all zeros
# dfs, better for visiting ALL zeros instead of ANY zeros
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        self.dfs(arr, start, visited) 
        for i, m in enumerate(arr):
            if m == 0 and i in visited:
                return True
        return False
        
    
    def dfs(self, arr, i, visited):
        visited.add(i)
        if i + arr[i] < len(arr) and i + arr[i] not in visited:
            self.dfs(arr, i + arr[i], visited)
        if i - arr[i] >= 0 and i - arr[i] not in visited:
            self.dfs(arr, i - arr[i], visited)

# method 3, bfs solution, one pass

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if len(arr) == 0 or len(arr) <= start or start < 0:
            return False
        q = [start]
        visited = set()
        while q:
            idx = q.pop(0)
            if arr[idx] == 0:
                return True
            visited.add(idx)
            left = idx - arr[idx]
            right = idx + arr[idx] 
            if left >= 0 and left not in visited:
                q.append(left)
            if right < len(arr) and right not in visited:
                q.append(right)
        return False
