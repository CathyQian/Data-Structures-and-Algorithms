"""
Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:

Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Constraints:

1 <= days <= weights.length <= 5 * 104
1 <= weights[i] <= 500

"""

# binary search
# Time complexity: O(N*log(S)), where N is the number of packages (i.e., size of the weights vector) and S is the total weight of all the packages.
# The reason for this time complexity is the binary search algorithm that is used to find the least weight capacity of the ship. In the worst case, 
# the binary search algorithm performs log(S) iterations, and for each iteration, it needs to traverse the entire weights vector, which takes O(N) time. 
# Therefore, the overall time complexity of the algorithm is O(N*log(S)).

# Space complexity: O(1)

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxweight, totalweight = -1, 0
        for weight in weights:
            maxweight = max(maxweight, weight)
            totalweight += weight
        
        # binary search
        left, right = maxweight, totalweight
        while left <= right: # break condition: left >= right
            mid = left + (right - left)//2
            daysneeded, curweight = 1, 0
            for weight in weights:
                if curweight + weight > mid:
                    daysneeded += 1
                    curweight = 0
                curweight += weight
            if daysneeded > days: # needs to increase mid
                left = mid + 1
            else:
                right = mid - 1

        return left