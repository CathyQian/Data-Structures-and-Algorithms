"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible
for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course
             0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency
matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
"""
solution:有向图,比其他结构都麻烦,先看看有没有环, 再用dfs or bfs搜索, 看长度是否吻合
https://blog.csdn.net/fuxuemingzhu/article/details/82951771
https://zhuanlan.zhihu.com/p/65238455
http://bookshadow.com/weblog/2015/05/07/leetcode-course-schedule/  -- topological sort
"""

# bfs, adjacency_list + in_degree list
class Solution(object):
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        in_degree = {num : 0 for num in range(numCourses)} # required
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
            
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        count = 0
        while queue:
            c = queue.popleft()
            count += 1
            for d in graph[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)
        if count < numCourses:# peeled all the onion
            return False
        return True   

# DFS + recusion stack
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.dependencies = defaultdict(list)
        for pre in prerequisites:
            self.dependencies[pre[0]].append(pre[1]) # opposite from bfs
        
        visited, stacked = [False]*numCourses, [False]*numCourses
        for course in range(numCourses):
            if visited[course] == False:
                if self.ispossible(course, visited, stacked) == False :
                    return False
        return True
        
    def ispossible(self, course, visited, stacked):
        visited[course] = True
        stacked[course] = True
        for pre in self.dependencies[course]:
            if visited[pre] == False:
                if self.ispossible(pre, visited, stacked) == False:
                    return False
            elif stacked[pre] == True:
                return False
        stacked[course] = False
        return True

#using color save O(n) space complexity compared to recursion stack
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.dependencies = defaultdict(list)
        for i in range(numCourses):
            self.dependencies[i]
        for pre in prerequisites:
            self.dependencies[pre[0]].append(pre[1])
        
        status = [0]*numCourses
        for course in range(numCourses):
            if status[course] == 0:
                if self.ispossible(course,status) == False :
                    return False
        return True
        
    def ispossible(self, course,status):
        status[course] = 1
        for pre in self.dependencies[course]:
            if status[pre] == 0:
                if self.ispossible(pre, status) == False:
                    return False
            elif status[pre] == 1:
                return False
        status[course] = 2
        return True
