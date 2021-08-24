"""
Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that 
lie on the same straight line.

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

 

Constraints:

    1 <= points.length <= 300
    points[i].length == 2
    -104 <= xi, yi <= 104
    All the points are unique.

"""
class Solution:
    def maxPoints(self, points):
        l = len(points)
        m = 0
        for i in range(l):
            dic = {'i': 1}
            same = 0
            for j in range(i+1, l):
                tx, ty = points[j][0], points[j][1]
                if tx == points[i][0] and ty == points[i][1]: # same points
                    same += 1
                    continue
                if points[i][0] == tx: # same x
                    slope = 'i'
                else: # different x, differnt y
                    slope = (points[i][1]-ty) * 1.0 /(points[i][0]-tx)
                if slope not in dic: 
                    dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m
