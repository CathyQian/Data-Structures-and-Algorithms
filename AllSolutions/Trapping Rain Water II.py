"""
Trapping Rain Water II

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

 

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

 

Constraints:

    1 <= m, n <= 110
    0 <= heightMap[i][j] <= 20000


"""

import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False]*n for _ in range(m)]        
        minheap = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    visited[i][j] = True
                    heapq.heappush(minheap, (heightMap[i][j], i, j))           

        while minheap:
            (h, r, c) = heapq.heappop(minheap)
            for x, y in directions:               
                if r+x >= 1 and r+x < m - 1 and c+y >= 1 and c+y < n - 1 and not visited[r+x][c+y]:
                    res += max(0, h - heightMap[r+x][c+y])
                    heapq.heappush(minheap, (max(h, heightMap[r+x][c+y]), r+x, c+y))
                    visited[r+x][c+y] = True
        
        return res