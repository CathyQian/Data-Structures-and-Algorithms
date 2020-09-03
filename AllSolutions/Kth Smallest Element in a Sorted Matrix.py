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
        N = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]
        
        while l <= r:
            mid = (l + r)>>1
            high = N - 1
            count = 0
            for row in range(N):
                while high > -1 and matrix[row][high] > mid:
                    high -= 1
                count += high + 1
            
            if count >= k :
                r = mid - 1
            else:
                l = mid + 1
        return l


# Solution 2: use heap. Don't need to put all elements in the heap. Instead, put the smallest element in
# the heap first, pop it, then put the next possible targets into the heap; pop min element again. Repeat
# k times. The kth element is the targeted kth smallest element.

# keep in note that element in the first column reach both its right and bottom element;
# other elements reach only its right elements.

# 1) Build a min heap which takes O(n) time (worst case)
# 2) Heapify k times which takes O(kLogn) time.(worst case)
# Therefore, overall time complexity is O(n + kLogn) time.

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return None

        m, n = len(matrix), len(matrix[0])

        q = [(matrix[0][0], 0, 0)]
        for _ in range(k):
            ans, i, j = heapq.heappop(q)

            # add its right and below elements into the heap, they are the next smallest elements
            if j == 0 and i + 1 < m:
                heapq.heappush(q, (matrix[i+1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j+1], i, j + 1))

        return ans