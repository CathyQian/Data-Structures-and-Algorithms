"""
Knight Dialer


"""
# DFS, time limit exceeded (too many repeated steps)
class Solution:
    def knightDialer(self, n: int) -> int:
        phonepad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
        cnt = 0
        for i in range(4):
            for j in range(3):
                if str(phonepad[i][j]).isdigit():
                    self.dfs(phonepad, i, j, n-1, cnt)
        return cnt%(10**9 + 7)

    def dfs(self, phonepad, i, j, remainsteps, cnt):
        if remainsteps == 0:
            cnt += 1
        else:
            for x, y in [(i+2, j+1), (i+2, j-1), (i-2, j+1), (i-2, j-1), (i+1, j+2), (i-1, j+2), (i+1, j-2), (i-1, j-2)]:
                if 0 <= x < 4 and 0 <= y < 3 and str(phonepad[x][y]).isdigit():
                    self.dfs(phonepad, x, y, remainsteps-1, cnt)
        return

# DFS + memo, a generic version
import collections
class Solution:
    def knightDialer(self, n: int) -> int:
        phonepad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
        self.memo = collections.defaultdict(int)
        ans = 0
        for i in range(4):
            for j in range(3):
                if str(phonepad[i][j]).isdigit():
                    ans += self.dfs(phonepad, i, j, n-1)
        return ans%(10**9 + 7)

    def dfs(self, phonepad, i, j, remainsteps):
        if (i, j, remainsteps) not in self.memo: 
            if remainsteps == 0:
                self.memo[(i, j, 0)] = 1    
            else:
                cnt = 0
                for x, y in [(i+2, j+1), (i+2, j-1), (i-2, j+1), (i-2, j-1), (i+1, j+2), (i-1, j+2), (i+1, j-2), (i-1, j-2)]:
                    if 0 <= x < 4 and 0 <= y < 3 and str(phonepad[x][y]).isdigit():
                        cnt += self.dfs(phonepad, x, y, remainsteps-1)
                self.memo[(i, j, remainsteps)] = cnt
        return self.memo[(i, j, remainsteps)]


# dfs + memo (too many duplicated steps)
class Solution:
    def knightDialer(self, n: int) -> int:
        # find the number of next move at each number
        self.next_move = {1: [6, 8], 2: [7, 9], 3: [4, 8],
                          4: [3, 9, 0], 5: [], 6: [0, 1, 7], 
                          7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        self.dp = collections.defaultdict(lambda: None)
        
        ans = 0
        for i in range(10):
            ans = (ans + self.dfsFind(i, n - 1))%(10**9+7)
        return ans
        
    def dfsFind(self, i, n):
        # recursion solution
        if n == 0:
            self.dp[i, n] = 1
            
        elif n == 1:
            self.dp[i, n] = len(self.next_move[i])
        
        if self.dp[i, n] is None:
            t_cnt = 0
            for ni in self.next_move[i]:
                t_cnt += self.dfsFind(ni, n - 1)
            self.dp[i, n] = t_cnt
        
        return self.dp[i, n]