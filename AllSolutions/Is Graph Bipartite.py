'''
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.
'''

'''
Analysis: We can start by coloring nodes with two different colors (1 and -1) and the color of each node should be different from its neighbors. If we find
any node with the same color as its neighbors, the graph is not bipartite (return False). 
Coloring nodes can be done either using DFS or BFS. 
BFS: start with any nodes (or node 0 for simplicity), color it with 1, then color its neighbors with -1 and put them in a queue or stack for coloring in the next round.
DFS: start with any nodes (or node 0 for simplicity), color it with 1, then color its neighbors with -1 and do DFS to color their neighbors etc. Return False if found 
node and its neighbor are the same color.
'''

import collections

# BFS solution
class Solution(object):
    def isBipartite(self, graph):
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 1
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if neighbor not in color:
                            stack.append(neighbor)
                            color[neighbor] = color[node] * (-1)
                        elif color[neighbor] == color[node]:
                            return False
        return True
    

# Time Complexity: O(N+E), where NNN is the number of nodes in the graph, and EEE is the number of edges. We explore each node once when 
# we transform it from uncolored to colored, traversing all its edges in the process.
# Space Complexity: O(N)O(N)O(N), the space used to store the color.

# DFS solution
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        color = {}
        for i in range(len(graph)):
            if i not in visited:
                color[i] = 1
                if not self.dfs(graph, i, color, visited):
                    return False
        return True

    def dfs(self, graph, curr, color, visited):
        visited.add(curr)
        for neighbor in graph[curr]:
            if neighbor in visited:
                if color[neighbor] == color[curr]:
                    return False
            else:
                color[neighbor] = color[curr] * (-1)
                if not self.dfs(graph, neighbor, color, visited):
                    return False
        return True
