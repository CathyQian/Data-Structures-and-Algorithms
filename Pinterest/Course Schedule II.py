"""
Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

Note:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.


"""

# dfs following topological sort alogrithm in Geeks&Geeks
# Main difference is to use different label of a node before and after recursion to detect cycle (!!!!)

from collections import defaultdict
class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        self.adj_list = defaultdict(list)
        for dest, src in prerequisites:
            self.adj_list[src].append(dest)

        self.topological_sorted_order = []
        self.has_cycle = False

        # By default all vertces are 0 -- unvisited, 1 --- visited but may be visited again if there is cycle,
        # 2 --- visited and will not be visited again, put in stack
        self.color = {k: 0 for k in range(numCourses)}
        
        for vertex in range(numCourses):
            if self.color[vertex] == 0:
                self.dfs(vertex)
            if self.has_cycle:
                break

        return [] if self.has_cycle else self.topological_sorted_order[::-1]
    
    def dfs(self, node):
            # Don't recurse further if we found a cycle already
            if self.has_cycle:
                return

            # Start the recursion
            self.color[node] = 1

            # Traverse on neighboring vertices
            if node in self.adj_list: # node may not in adj list
                for neighbor in self.adj_list[node]:
                    if self.color[neighbor] == 0:
                        self.dfs(neighbor)
                    elif self.color[neighbor] == 1: # this node is visited again in the same loop
                        self.has_cycle = True
                        return

            # Recursion ends. We mark it as black
            self.color[node] = 2
            self.topological_sorted_order.append(node)