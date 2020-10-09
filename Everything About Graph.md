## graph representation (both directional and undirectional)
There are two most commonly used representation of graph:
- adjacency matrix
    - 2D array of size V*V (V = number of vertices of a graph)
    - adj[i][j] = 1 indicates there is an edge from vertix i to vertex j
    - for weighted graph, adj[i][j] = weight
    - adjacency matrix for undirected graph is always symmetric
    - Pros: Retrieving or removing an edge takes O(1) time
    - Cons: Consumes more space O(V^2). Adding a vertex is O(V) time
- adjacency list
    - use a list of arrays to represent the edges in the graph. The size of the array is equal to the number of vertices
    - Pros: Saves space O(|V|+|E|) (vertix list + edge adjacency list) . In the worst case, there can be C(V, 2) number of edges in a graph thus consuming O(V^2) space. Adding a vertex takes O(1) time.
    - Cons: Queries like whether there is an edge from vertex u to vertex v are not efficient and can be done O(V).


```Python
# A simple representation of graph using adjacency matrix
class Graph:
    def __init__(self, numvertex): # predefine space for the graph
        self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex # predefine maximum number of vertex
        self.vertices = {} # vertix val: index
        self.verticeslist = [0]*numvertex # host vertices by their index order

    def set_vertex(self, idx, vtx):
        if 0 <= idx <= self.numvertex:
            self.vertices[vtx] = idx
            self.verticeslist[idx] = vtx

    def set_edge(self, frm, to, cost=1):
        frm = self.vertices[frm] # O(1) time to find index of an element
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost
        # for directed graph do not add this
        self.adjMatrix[to][frm] = cost

    def get_vertex(self):
        return self.verticeslist

    def get_edges(self):
        edges = []
        for i in range (self.numvertex):
            for j in range (self.numvertex):
                if (self.adjMatrix[i][j] != -1):
                    edges.append((self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j]))
        return edges
        
    def get_matrix(self):
        return self.adjMatrix

G = Graph(6)
G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
G.set_edge('a','e',10)
G.set_edge('a','c',20)
G.set_edge('c','b',30)
G.set_edge('b','e',40)
G.set_edge('e','d',50)
G.set_edge('f','e',60)
print("Vertices of Graph")
print(G.get_vertex())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())
```

```Python
# The adjacency list representation of the graph
# no place to host the edge weight if they are not constant
# A class to represent the adjacency list of the node 
import collections
class Graph():      
    def __init__(self, V):          
        self.V = V # number of vertices, from 0 to V-1         
        self.graph = collections.defaultdict(list) # adjacency list

    def addEdge(self, v, w): # undirectional graph  
        self.graph[v].append(w)           
        self.graph[w].append(v)  

# Driver program to the above graph class 
if __name__ == "__main__": 
	V = 5
	graph = Graph(V) 
	graph.addEdge(0, 1) 
	graph.addEdge(0, 4) 
	graph.addEdge(1, 2) 
	graph.addEdge(1, 3) 
	graph.addEdge(1, 4) 
	graph.addEdge(2, 3) 
	graph.addEdge(3, 4) 
 
ref: https://www.geeksforgeeks.org/graph-and-its-representations/

```

## topological sort (include dfs or bfs node traversal)
Topological sort is a linear ordering of vertices such that for every directed edge u->v, vertex u comes before v
in the ordering. It only works for directed acryclic graph (DAG). It is used to determine dependencies for events/programs/courses. 

**Topological orders are not unique!**
Topological sort can be achieved using either dfs or bfs. Using dfs can get all topological orders if starting from different points. See Alien Dictionary for code.

## topology algorithm
It is all about dfs post-order, aming to identify structures, depths and connections of graphs.
Typical use scenarios include:
    - find shortest path (shortest path for DAG)
    - find distances along
    - comparing of graph structures
    
Isomorphism: if two trees are exactly the same

## directional graph to tree (include cycle detection)

**Both DFS and BFS can be used to detect a cycle in a Graph. DFS for a connected graph produces a tree. There is a cycle in a graph only if there is a back edge present in the graph. A back edge is an edge that is joining a node to itself (self-loop) or one of its ancestor in the tree produced by DFS.** Think in terms of a tree when doing dfs. Alternatively, you can also use the generic template below to tell if a graph has cycle or not.

If a **directed graph** can be converted to tree, it needs to meet the following criteria:
- all graph nodes are connected
- there is no cycle in the graph
- each node only have one parent except one without parent (that's the root, find the root first)

```Python
import collections

# represent a graph using adjacency matrix
class Graph():      
    def __init__(self, V):          
        self.V = V # number of vertices, from 0 to V-1         
        self.graph = collections.defaultdict(list) # adjacency list
        self.in_degree = collections.defaultdict(int)
    def addEdge(self, v, w): # directional graph  v -> w
        self.graph[v].append(w)           
        self.in_degree[w] += 1

class Solution:
    def isTree(self, graph):
        visited = [False] * graph.V 

        # find the root of the tree if it exist
        root = None
        for node, num_parent in self.in_degree.items():
            if num_parent > 1:
                return False
            if num_parent == 0 and not root:
                root = child
            if num_parent == 0 and root:
                return False
        if not root: # root not found
            return False    
        
        # start to detect the cycle from the root
        if self.hasCycle(graph, root, visited, -1): # this function can be changed to simply bfs or dfs the graph
            return False 
        for i in range(graph.V): # even if there is no cycle, the graph may not be all connected              
            if not visited[i]:                  
                return False            
        return True 

    def hasCycle(self, graph, v, visited, parent): # optional
        # detect cycle in directed graph given the root of the graph is found
        # this is different if the root is unknown or don't exist         
        visited[v] = True         
        for i in graph.graph[v]:              
            if not visited[i]:                 
                if self.hasCycle(graph, i, visited, v):                      
                    return True             
            elif visited[i] and i != parent: # This node has more than one parent, cann't form a tree             
                return True         
        return False      
```

Below is the **generic dfs template to detect cycle in directed graph regardless of the topology of the tree**.
Refer to Alien Dictionary for bfs template.
```Python
import collections

# represent a graph using adjacency matrix
class Graph():      
    def __init__(self, V):          
        self.V = V # number of vertices, vertices name from 0 to V-1         
        self.graph = collections.defaultdict(list) # adjacency list

    def addEdge(self, v, w): # directional graph  v --> w
        self.graph[v].append(w)  

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
  
    def isCyclic(self): 
        # color: 0 --- unvisited, 1 --- currently visiting, 2 --- finished visiting
        self.color = [0]*self.V
        self.has_cycle = False    
        for vertex in range(self.V):
            if self.color[vertex] == 0:
                self.dfs(vertex)
            if self.has_cycle:
                break

        return self.has_cycle
  
```

## clone graph
```Python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: # edge case
            return None
        root = Node(node.val)
        visited = {node.val: root}
        q = [node] # host all visited nodes
        while q:
            new = q.pop(0)
            for n in new.neighbors: 
                if n.val not in visited: # check if already generated
                    visited[n.val] = Node(n.val)
                    q.append(n)
                visited[new.val].neighbors.append(visited[n.val])    # new is always been visited, this line is required regardless of n visited or not 
        return root
```

## unionfind -- Number of Islands II

https://leetcode.com/problems/number-of-islands-ii/

```Python
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]: # m, n not needed
        res = []
        islands = UnionFind()
        for (i, j) in positions:
            x = (i, j) # tuple can be key of dictionary, list can not.
            if x not in islands.parent:
                # add node if it doesn't exist
                islands.parent[x] = x # parent of itself
                islands.rank[x] = 0
                islands.count += 1
                # union with neighbors if possible
                for y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if y in islands.parent:
                        islands.union(x, y)
            res.append(islands.count)
        return res   

class UnionFind:
    def __init__(self):
        self.parent = {} # contain all nodes and their parents
        self.rank = {} # all nodes and rank
        self.count = 0 # number of subsets in the graph

    def find(self, x): # find root of x, point all nodes directly to the root --- called path compression, to tell if two nodes are in the same subset
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y): # every find or union operation will link node to the root of the set
        x, y = self.find(x), self.find(y)
        if x != y: # x, y not in the same set
            if self.rank[x] < self.rank[y]: # make sure self.rank[x] >= self.rank[y]
                x, y = y, x
            self.parent[y] = x # attach the shorter branch to the longer one
            if self.rank[x] == self.rank[y]: # union by rank
                self.rank[x] += 1
            self.count -= 1
            
```