"""
Alien Dictionary
"""

"""
input: ["ab", "abc"]
return: there is a chance that we can come up with a valid ordering


input: ["abc", "ab"]
return: "" (as it's impossible to figure out a valid ordering, lexicographically ab should come in front of abc)

The key point is to convert the problem into a directed graph problem. Build the adjacency list, then use bfs or 
dfs to figure out the directed order (similar as in Course Schedule II).
The difference between bfs and dfs is 1) the order of the adjacency list -- opposite 2) whether we need an in_degree dictionary to know if
it's time to put a node in the output list
"""

# bfs

from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set) # set not list
        in_degree = {c : 0 for word in words for c in word} # required

        # bfs traversal of graph (layer determined by the in_degree)
        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for w1, w2 in zip(words, words[1:]): # use of zip
            # Check that second word isn't a prefix of first word.
           if len(w2) < len(w1) and w2 == w1[:len(w2)]:
                return ""
            for c, d in zip(w1, w2):
                if c != d:
                    if d not in adj_list[c]: # need to check to avoid duplicated input
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        d = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = d.popleft()
            output.append(c)
            for v in adj_list[c]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    d.append(v)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output) # string operation



# dfs: reverse adj list

def alienOrder(self, words: List[str]) -> str:

    # Step 0: Put all unique letters into the adj list.
    self.adj_list = {c : [] for word in words for c in word}

    # Step 1: Find all edges and put them in adj_list.
    for w1, w2 in zip(words, words[1:]):
        # Check that second word isn't a prefix of first word.
        if len(w2) < len(w1) and w2 == w1[:len(w2)]:
                return ""
        for c, d in zip(w1, w2):
            if c != d: 
                self.adj_list[c].append(d)
                break

    # Step 2: Depth-first search.
    self.output = []
    self.color = {c:0 for word in words for c in word}
    self.has_cycle = False
    
    for vertex in range(len(self.color)):
        if self.color[vertex] == 0:
            self.dfs(vertex)
        if self.has_cycle:
            break

    if self.has_cycle:
        return ""

    return "".join(self.output[::-1])

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
        self.output.append(node)

 """
 get all possible order: use dfs, permute vertex in line 85
 can tell if all nodes in the graph is connected or not (starting from one node, see if all nodes can be visited or not) in undirectional graph
 
 """
