"""
Friend Circles

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a 
direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, 
otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.

 

Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

 

Constraints:

    1 <= N <= 200
    M[i][i] == 1
    M[i][j] == M[j][i]


"""
# undirectional graph (two directed graph), dfs to search for all linked elements, count how many dfs in total
# cannot use bfs now because it's impossible to define the in-degree

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0
        n = len(M)
        self.adj_dict = collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j] == 1:
                    self.adj_dict[i].append(j)
                    self.adj_dict[j].append(i)
        count = 0
        self.visited = [False] * n
        # dfs
        for i in range(n):
            if self.visited[i] == False:
                self.dfs(M, i)
                count += 1
        return count
        
    def dfs(self, M, i):
        self.visited[i] = True
        for n in self.adj_dict[i]:
            if self.visited[n] == False:
                self.dfs(M, n)
            
        
