"""
Best Meeting Point

Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

 

Example 1:

Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 6
Explanation: Given three friends living at (0,0), (0,4), and (2,2).
The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
So return 6.

Example 2:

Input: grid = [[1,1]]
Output: 1

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    grid[i][j] is either 0 or 1.
    There will be at least two friends in the grid.



"""

# In 1D, the best meeting point is the median of all points. Therefore, we just need to find the median of the y coordinates
# y_median and x coordiates x_median of all points, respectively. The best meeting point would be (y_median, x_median).
# detailed explaination: https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm?rq=1

# Time complexity O(mn) + O(KlogK) # K is number of houses max(K) = nm; consider worst case senario -->
# Time complexity: O(nm log (nm)), space complexity: O(nm), where n = len(grid), m = len(grid[0])

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        # put x and y in list
        x_list, y_list = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x_list.append(i)
                    y_list.append(j)
                    
        # find median of x and y list
        x_list.sort()
        y_list.sort()
        dim = len(x_list)
        x_median = x_list[dim//2] # if len is even, either len//2 or len//2-1 works
        y_median = y_list[dim//2] # if len is odd, only len//2 works
        
        # calculate distance
        res = 0
        for i in range(len(x_list)):
            res += abs(x_median - x_list[i]) + abs(y_median-y_list[i])
        
        return res