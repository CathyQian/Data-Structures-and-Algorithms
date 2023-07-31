"""
Number of Ways to Build Sturdy Brick Wall

You are given integers height and width which specify the dimensions of a brick wall you are building. You are also given a 0-indexed array of unique integers bricks, where the ith brick has a height of 1 and a width of bricks[i]. You have an infinite supply of each type of brick and bricks may not be rotated.

Each row in the wall must be exactly width units long. For the wall to be sturdy, adjacent rows in the wall should not join bricks at the same location, except at the ends of the wall.

Return the number of ways to build a sturdy wall. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:


Input: height = 2, width = 3, bricks = [1,2]
Output: 2
Explanation:
The first two walls in the diagram show the only two ways to build a sturdy brick wall.
Note that the third wall in the diagram is not sturdy because adjacent rows join bricks 2 units from the left.
Example 2:

Input: height = 1, width = 1, bricks = [5]
Output: 0
Explanation:
There are no ways to build a sturdy wall because the only type of brick we have is longer than the width of the wall.

Constraints:

1 <= height <= 100
1 <= width <= 10
1 <= bricks.length <= 10
1 <= bricks[i] <= 10
All the values of bricks are unique.

"""

"""
ref: https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/solutions/1797403/python-3-dfs-adjacency-list-explanation/
Time Complexity:
It's hard to use input parameters to represent the time complexity, so I will make an estimation using worst test case
Given the most complicated input
100
10
[1,2,3,4,5,6,7,8,9,10]
Then len(combos) == 512, there are 100 level at max, so with @cache, the max computation during DFS is about O(51200)
Finding possible neighbor takes 512*512=O(262144)
In total time is at O(10^5) level
Space is capped by the adjacency list d, which is O(10^5)
"""

class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        options = [] # number of permutations
        # trick 1: DFS to figure out numbers of combo (permutation problem), record breaks instead of bricks
        def fill_one_row(breaks, length):
            if length == width:
                options.append(tuple(breaks[:-1]))
                return
            for b in bricks:
                if length + b <= width:
                    breaks.append(length + b)
                    fill_one_row(breaks, length + b)
                    breaks.pop() # backtracking
        
        fill_one_row([], 0)
        
        # print(options)
        # note each option can be used unlimited times --> DFS no need to consider remove used elements
        # find neighbors
        valid_neighbors = defaultdict(set)
        
        for i in range(len(options)):
            for j in range(i, len(options)):
                if not set(options[i]) & set(options[j]): # no overlaps
                    valid_neighbors[options[i]].add(options[j])
                    valid_neighbors[options[j]].add(options[i])
        
        @cache # need cache otherwise TLE, another DFS here to figure out # of ways to pile up
        def count_ways(op, h):
            if h == height:
                return 1
            return sum([count_ways(op1, h+1) for op1 in valid_neighbors[op]]) % (10**9+7)
        
        return sum([count_ways(op, 1) for op in options]) % (10**9 + 7)