"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""

# Method1: direct search, O(n)

class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []
    
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1
        # start    
        if not output or output[-1][1] < new_start:
            output.append(newInterval)

        else:
            output[-1][1] = max(output[-1][1], new_end)
        # end
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)
        return output



# Method2: binary search to find the index of the left and right edge of the newInterval, be careful with bounds
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: 
        bounds = []
        for i in range(len(newInterval)):
            left, right = 0, len(intervals)-1
            while left <= right:
                mid = left+(right-left)//2
                if intervals[mid][0] <= newInterval[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            bounds.append([left, right])
            
        left_bound, right_bound = bounds[0][1], bounds[1][0]
        
        result = intervals[:left_bound+1]
        if not result or result[-1][1]<newInterval[0]:
            result.append(newInterval)
        else:
            result[-1][1]= max(result[-1][1], newInterval[1])
            
        for idx in range(left_bound+1, right_bound):
                result[-1][1]= max(result[-1][1], intervals[idx][1])
        return result + intervals[right_bound:]
