"""
The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).
Buildings Skyline Contour

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

    The number of buildings in any input list is guaranteed to be in the range [0, 10000].
    The input list is already sorted in ascending order by the left x position Li.
    The output list must be sorted by the x position.
    There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]

"""
from heapq import heappush, heappop
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        #using -h, because we need the seg with higher h be pushed first to the hori_segs corner [[1,2,1],[1,2,2],[1,2,3]]
        #place -h in front of r to avodid corner case [[3,10,20],[3,9,19],[3,8,18],[3,7,17],[3,6,16],[3,5,15],[3,4,14]]
        bud_start = [(l,-h,r) for l,r, h in buildings]
        bud_end = [(r,0,sys.maxsize) for _,r, _ in buildings]
        hori_segs = sorted(bud_start+bud_end)
        
        # check the max current height when we have a new horizontal segment if the new max height is different from
        # the previous max height, we get a new key point.
        cur_hi, result = [], [[0,0]]
        for l, h, r in hori_segs:
            heappush(cur_hi, (h,r))
            
            while l >= cur_hi[0][1]:
                heappop(cur_hi)
            
            new_hi = -cur_hi[0][0]
            if new_hi != result[-1][1]:
                result.append([l,new_hi])
        return result[1:]