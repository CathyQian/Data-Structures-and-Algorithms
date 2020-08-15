"""
Paint House

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of 
painting each house with a certain color is different. You have to paint all the houses such that no two adjacent 
houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0]
 is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and 
 so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.


"""
# only has three colors, much easier compared to Paint House II
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        row = [0, 0, 0]
        for r in costs:
            row[0], row[1], row[2] = r[0] + min(row[1], row[2]), r[1] + min(row[0], row[2]), r[2] + min(row[0], row[1])
        return min(row)

# usually use pre and cur two rows, but can be replaced by one row as shown above