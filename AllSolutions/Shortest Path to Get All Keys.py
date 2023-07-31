"""
Shortest Path to Get All Keys

You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

Example 1:


Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.
Example 2:


Input: grid = ["@..aA","..B#.","....b"]
Output: 6
Example 3:


Input: grid = ["@Aa"]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.

"""

# DFS solution --- Wrong
# Can walk back otherwise may not be able to pick up some keys; so can't block visited grids --> time limit exceed
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        if not grid or not grid[0]:
            return -1
        self.key_cnt = 0
        grid = [list(g) for g in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    start_i, start_j = i, j
                if grid[i][j] in 'abcdefghijklmnopqrstuvwxyz':
                    self.key_cnt += 1
        self.min_moves = sys.maxsize
        self.dfs(grid, start_i, start_j, [], 0)
        return self.min_moves if self.min_moves < sys.maxsize else -1

    def dfs(self, grid, i, j, visited_keys, steps):
        if len(visited_keys) == self.key_cnt:
            self.min_moves = min(self.min_moves, steps)
        else:
            temp = grid[i][j]  # WRONG, CAN WALK BACK
            grid[i][j] = '#' # WRONG, CAN WALK BACK
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#':
                    # lowercase letters, update visited_keys and steps, then go
                    if grid[x][y] in 'abcdefghijklmnopqrstuvwxyz':
                        #visited_keys.add(grid[x][y]) # update in-place, no return
                        self.dfs(grid, x, y, visited_keys +[grid[x][y]], steps + 1)
                    # empty cell or upper case letters with keys, update steps, then go
                    if (grid[x][y] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and grid[x][y].lower() in visited_keys) or grid[x][y] == '.':
                        self.dfs(grid, x, y, visited_keys, steps + 1)
            grid[i][j] = temp  # WRONG, CAN WALK BACK
        return
    
# BFS; Time complexity: O(mn), Space complexity: O(mn)
# the trick is add keys into the state to allow walk back but needs to be with a different keysets
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        start_i, start_j, cnt = 0, 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@": 
                    start_i, start_j = i, j
                elif grid[i][j].islower(): 
                    cnt += 1
        
        ans = 0
        visited = {(start_i, start_j, "")} # state = (col, row, keys), can walk over the same cell, but with a different keyset; otherwise the steps found is not optimal
        queue = [(start_i, start_j, "")]
        while queue: 
            newq = [] # each layer has the same number of steps
            for i, j, keys in queue: 
                if len(keys) == cnt: # find all keys
                    return ans 
                for x, y in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]: 
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != "#": # empty space or key or lock
                        kk = keys 
                        if grid[x][y].islower() and grid[x][y] not in kk: # key and hasn't been picked up before to guarantee uniqueness
                            #kk |= 1 << ord(grid[x][y]) - 97 # pick up this key
                            kk += grid[x][y]
                            kk = ''.join(sorted(kk))
                        if (x, y, kk) in visited or (grid[x][y].isupper() and grid[x][y].lower() not in kk): # this state has been seen before or this is lock but without key
                            continue 
                        newq.append((x, y, kk))
                        visited.add((x, y, kk))
            ans += 1
            queue = newq
        return -1