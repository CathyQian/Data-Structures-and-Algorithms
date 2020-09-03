"""
Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the
minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1

"""
# method 1: order all starting and ending points (make sure to put end before start if same value), scan from left to right
# if start, count + 1, else count -1; use res to record max(count) along the way
# O(NlogN)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = []
        for (s, e) in intervals:
            points.append((s, 's'))
            points.append((e, 'e'))
        points.sort()
        res, count = 0, 0
        for (x, y) in points:
            if y == 's':
                count += 1
            else:
                count -= 1
            res = max(res, count)
        return res

# method 2: similar to method 1, but use two list instead of one list
# O(NlogN)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for (s, e) in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()
        res, count = 0, 0
        ps, pe = 0, 0
        while ps < len(start) and pe < len(end):
            if start[ps] < end[pe]:
                count += 1
                res = max(res, count)
                ps += 1
            else: # start[ps] >= end[pe], pay special attention to '='
                count -= 1
                pe += 1
     
        return res
        
# method 3, use minHeap