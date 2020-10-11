"""
Graph Valid Tree

给你⼀一个undirectional graph，问他能不不能成为⼀一个tree
"""

"""
Attention: not binary tree
undirectional graph (= 2 directional graph with cycle) to tree --- 1) nodes all connected 2) no cycle, dfs (adj_list), can't use template for directional graph

directional graph to tree --- 1) nodes all connected, 2) no cycle, 3) no nodes has more than one ancestor, bfs (ajd_list + in_degree)
"""

# ref: https://www.geeksforgeeks.org/detect-cycle-undirected-graph/

from collections import defaultdict  
class Graph():      
    def __init__(self, V):          
        self.V = V # number of vertices, from 0 to V-1         
        self.graph  = defaultdict(list) # adjacency list

    def addEdge(self, v, w): # undirectional graph  
        self.graph[v].append(w)           
        self.graph[w].append(v)   

class Solution:
    def isTree(self, graph):   # can be separate function or 
        visited = [False] * graph.V  
        if self.hasCycle(graph, 0, visited, -1): # a tree: one node can dfs to access any other nodes
            return False 
        for i in range(graph.V): # even if there is no cycle, the graph may not be all connected              
            if not visited[i]:                  
                return False            
        return True 

    def hasCycle(self, graph, v, visited, parent):          
        visited[v] = True         
        for i in graph.graph[v]:              
            if not visited[i]:                 
                if self.hasCycle(graph, i, visited, v):                      
                    return True             
            elif visited[i] and i != parent: # only when i == parent --> no cycle                  
                return True         
        return False       

g1 = Graph(5)  
g1.addEdge(1, 0)  
g1.addEdge(0, 2) 
g1.addEdge(0, 4) 
g1.addEdge(0, 3)  
g1.addEdge(3, 4)  
test = Solution()
print("Graph is a Tree" if test.isTree(g1) else "Graph is a not a Tree")

# dfs solution, slight modification from topological sort template (I personally like this one better)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.adj_list = collections.defaultdict(set)
        for edge in edges:
            self.adj_list[edge[0]].add(edge[1])
            self.adj_list[edge[1]].add(edge[0])
        
        self.visited = {i: 0 for i in range(n)}
        self.has_cycle = False
       
        self.dfs(0, -1) # start from any node, do one dfs
        if self.has_cycle:
            return False
      
        for i in range(n):
            if self.visited[i] == 0:
                return False
        return True
    
    def dfs(self, i, parent):
        self.visited[i] = 1
        if i in self.adj_list:
            for neighbor in self.adj_list[i]:
                if self.visited[neighbor] == 1 and neighbor != parent: # make sure neighbor != parent as it's undirectional graph
                    self.has_cycle = True
                    return 
                if self.visited[neighbor] == 0:
                    self.dfs(neighbor, i)
                    if self.has_cycle:
                        return
        self.visited[i] = 2
        
