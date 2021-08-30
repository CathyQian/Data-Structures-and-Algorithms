"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth 
smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
1 5 9
2 6 16
13 15 17
1; 2, 5; 5,6,13; 6,9,13; 9, 13, 16; 13, 16; 15, 16; 16, 17; 17
1; 2,5; 3,6,5;5,6,7; 6, 7, 9; 7, 9, 10; 9, 10,11 ; 10, 11
"""

"""
analysis: This matrix with each row and column in ascending order are quite common in Leetcode. Similar 
problems include 240.search a 2D matrix. Key is to start from the right top corner and move left (if smaller)
or down (if bigger)

Kth largest/smallest --> maxheap or minheap (Python default)
"""
# Solution 1: binary search (not an ideal method), it's complicated and not easy to be adopted for similar
# problem. Similar to Leetcode 240.  (don't understand yet)

class Solution:
    def kthSmallest(self, matrix, k):
        if not matrix or not matrix[0]:
         return None
        n = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]
        
        while l <= r:
            mid = (l + r)//2
            high = n - 1
            count = 0
            for row in range(n):
                while high > -1 and matrix[row][high] > mid:
                    high -= 1
                count += high + 1
            
            if count >= k :
                r = mid - 1
            else:
                l = mid + 1
        return l

# Solution 2 (preferred): use heap. Don't need to put all elements in the heap. Instead, put the smallest element in
# the heap first, pop it, then put the next possible targets into the heap; pop min element again. Repeat
# k times. The kth element is the targeted kth smallest elements

# time complexity: O(klogk), space: O(k)

class Solution:
    def kthSmallest(self, matrix, k):
        if not matrix or not matrix[0]:
            return None
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        visited = {(0,0)} # needed to avoid putting the same elements into the heap multiple times
        for _ in range(k):
            ans, i, j = heapq.heappop(q) # O(1)
            if i + 1 < m and (i+1, j) not in visited:
                heapq.heappush(q, (matrix[i+1][j], i + 1, j)) # O(logk)
                visited.add((i+1, j))
            if j + 1 < n and (i, j+1) not in visited:
                heapq.heappush(q, (matrix[i][j+1], i, j + 1))
                visited.add((i, j+1))
        return ans
