"""
Reaching Points

A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

    sx, sy, tx, ty will all be integers in the range [1, 10^9].

"""

# method 1: work forward (dfs + memo),  will result in time exceed limit
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        self.memo = {}
        return self.reachingPointsHelper(sx, sy, tx, ty)
    
    def reachingPointsHelper(self, sx, sy, tx, ty):
        if (sx, sy) not in self.memo:
            if sx == tx and sy == ty:
                self.memo[(sx, sy)] = True
            elif sx > tx or sy > ty: # not put in memo
                return False
            else:
                if self.reachingPointsHelper(sx+sy, sy, tx, ty) or self.reachingPointsHelper(sx, sx+sy, tx, ty):
                    self.memo[(sx, sy)] = True
        return self.memo[(sx, xy)]

# method 2: work backword, no memo needed because there's only one path
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else: # ty == sy
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else: # tx == sx
                    return (ty - sy) % tx == 0
        return tx == sx and ty == sy
     
