"""
Escape a Large Maze

In a 1 million by 1 million grid, the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.

We start at the source square and want to reach the target square.  Each move, we can walk to a 
4-directionally adjacent square in the grid that isn't in the given list of blocked squares.

Return true if and only if it is possible to reach the target square through a sequence of moves.


Example 1:

Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation: 
The target square is inaccessible starting from the source square, because we can't walk outside the grid.

Example 2:

Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation: 
Because there are no blocked cells, it's possible to reach the target square.


Note:

    0 <= blocked.length <= 200
    blocked[i].length == 2
    0 <= blocked[i][j] < 10^6
    source.length == target.length == 2
    0 <= source[i][j], target[i][j] < 10^6
    source != target


"""
# DFS, time exceed limit
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True
        elif target in blocked:
            return False
        res = self.dfs(blocked, source, target)
        return True if res else False
    
    def dfs(self, blocked, start, target):
        if start == target:
            return True
        
        for x, y in [(start[0]+1, start[1]), (start[0]-1, start[1]), (start[0], start[1]+1), (start[0], start[1]-1)]:
            if 0 <= x < 10e6 and 0 <= y < 10e6 and [x,y] not in blocked:
                print(x, y)
                blocked.append(start)
                res = self.dfs(blocked, [x, y], target)
                blocked.remove(start)
                if res:
                    return True
        return False

# dfs, from a completely new perspective
# if cannot connect, either source or target are trapped. Using len(blocked) elements, the largest area it
# can trap is approximately len(B)*len(B)/2 (diagonally along with two borders)
# if either source or target can access more than such steps or meet each other, return True; else False

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        bkset = set(map(tuple, blocked))
        return self.findtarget(bkset, set(), tuple(source), tuple(target), 0) and \
               self.findtarget(bkset, set(), tuple(target), tuple(source), 0)

    def findtarget(self, bkset, visited, source, target, step):
        if step >= len(bkset)*len(bkset)/2 or source == target:
            return True
        s0, s1 = source[0], source[1]
        visited.add(source)
        for x, y in [(s0+1,s1), (s0-1,s1), (s0,s1+1), (s0,s1-1)]:
            if 0 <= x < 10e6 and 0 <= y < 10e6 and (x, y) not in visited and (x, y) not in bkset:
                if self.findtarget(bkset, visited, (x, y), target, step+1):
                    return True
        return False