"""
Employee Free Time

We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]

 

Constraints:

    1 <= schedule.length , schedule[i].length <= 50
    0 <= schedule[i].start < schedule[i].end <= 10^8

"""

# It doesn't matter how many emploees are there. Put all Intervals in a list and convert to a minHeap.
# Take elements out of the heap one by one, record previous end and the new start to see if there is a gap. 
# If yes, record that gap. Iterate until the minHeap is empty.

import heapq
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for s in schedule:
            for ss in s:
                intervals.append([ss.start, ss.end])
        heapq.heapify(intervals)
        _, e0 = heapq.heappop(intervals)
        res = []
        while intervals:
            s1, e1 = heapq.heappop(intervals)
            if s1 > e0:
                new = Interval(start=e0, end=s1)
                res.append(new)
                e0 = e1
            else:
                e0 = max(e0, e1)
        return res
            
"""

# compare with Interval List Intersections, very similar problem but different solution logic
- Interval list intersections: known there are only Two list, so can use two pointers; employee free time can have many
employees, so can't use pointers
- The number of employees/intervals doesn't matter in both cases
- Interval list intersections: intervals are already sorted, so pointers can move from left to right
- Employee free time: need to sort first, sort unknwon number of lists ---> minHeap
"""


# the above solution doesn't use the sorted property in each employee list --- so how?
# k employees, on average m intervals per employee --> mk intervals in total
# k >> m or m >> k
# time: O(n), space: O(k)
import heapq
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for i, sch in enumerate(schedule):
            intervals.append((sch[0].start, sch[0].end, i, 0))
        heapq.heapify(intervals) # O(k)
        _, e0, i, j = heapq.heappop(intervals)
        k = len(schedule)
        idx = [0]*k # record indexes
        res = []
        while intervals:# O(n-k)
            # not sure how to deal with else
            while j >= 0 and j+1 >= len(schedule[i]): # when j overflow schedule[i]
                idx[i] = -1
                i = (i+1)%k # critical, point to the next available list
                j = idx[i]
            if j >= 0 and j + 1 < len(schedule[i]):
                heapq.heappush(intervals, (schedule[i][j+1].start, schedule[i][j+1].end, i, j+1))
                idx[i] += 1
            s1, e1, i, j = heapq.heappop(intervals)
            if s1 > e0:
                new = Interval(start=e0, end=s1)
                res.append(new)
                e0 = e1
            else:
                e0 = max(e0, e1)
        return res
