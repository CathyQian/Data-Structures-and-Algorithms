"""
The Maze

There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).


Example 1:

Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.

Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false


Constraints:

    1 <= maze.length, maze[i].length <= 100
    maze[i][j] is 0 or 1.
    start.length == 2
    destination.length == 2
    0 <= startrow, destinationrow <= maze.length
    0 <= startcol, destinationcol <= maze[i].length
    Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
    The maze contains at least 2 empty spaces.


"""
# make sure don't do dfs again at the same point
# same point can be crossed again
# use tuple instead of list
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        self.row, self.col = len(maze), len(maze[0])             
        return self.dfs(maze, tuple(start), tuple(destination), set())

    def dfs(self, maze, start, dest, seen):
        if start == dest:
            return True
        seen.add(start)
        for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            x, y = start
            nx,ny = x+d[0], y+d[1]
            # keep rolling to the end
            while 0 <= nx < self.row and 0 <= ny < self.col and maze[nx][ny] != 1: # can be -1 or 0
                x += d[0]
                y += d[1]
                nx,ny = x+d[0], y+d[1]
            if (x, y) not in seen:
                if self.dfs(maze, (x, y), dest, seen):
                    return True
        return False
