"""
Interval List Intersections

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

 

Note:

    0 <= A.length < 1000
    0 <= B.length < 1000
    0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

"""

"""
Hidden information: there is no overlaps in the intervals in A or B alone.
Use of stack will make things complicated as we don't need to return stack information.
Tell if there is overlap: (A[i][0] >= B[j][0] and A[i][0] <= B[j][1]) or (B[j][0] >= A[i][0] and B[j][0] <= A[i][1])
"""
# time complexity: o(m+n)
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:   
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            if (A[i][0] >= B[j][0] and A[i][0] <= B[j][1]) or (B[j][0] >= A[i][0] and B[j][0] <= A[i][1]):
                res.append([max(A[i][0], B[j][0]), min([A[i][1], B[j][1]])])   
			# Move the pointer to find the next possible overlapped region
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j+=1
                 
        return res


# time complexity: ((m+n)log(m+n))  --- didn't use the sorted property of each list
from heapq import heapify, heappop
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        intervals, intersections = [], []
        if len(firstList) == 0 or len(secondList) == 0:
            return []

        for inter in firstList:
            intervals.append((inter[0], inter[1], 0))
        for inter in secondList:
            intervals.append((inter[0], inter[1], 1))
        heapify(intervals) 
        
        _, e0, i0 = heappop(intervals)
        while intervals: 
            s1, e1, i1 = heappop(intervals)
            if i0 != i1 and s1 <= e0:
                intersections.append([s1, min(e0, e1)])
            if e1 > e0:
                _, e0, i0 = _, e1, i1
        
        return intersections

