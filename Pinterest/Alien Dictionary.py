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
        adj_list = defaultdict(set)
        in_degree = {c : 0 for word in words for c in word} # dictionary comprehension

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]): # use of zip
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            # if nothing has been done in the for loop
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output) # string operation



# dfs

def alienOrder(self, words: List[str]) -> str:

    # Step 0: Put all unique letters into the adj list.
    reverse_adj_list = {c : [] for word in words for c in word}

    # Step 1: Find all edges and put them in reverse_adj_list.
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):
            if c != d: 
                reverse_adj_list[d].append(c)
                break
        else: # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word): 
                return ""

    # Step 2: Depth-first search.
    seen = {} # False = grey, True = black.
    output = []
    def visit(node):  # Return True iff there are no cycles.
        if node in seen:
            return seen[node] # If this node was grey (False), a cycle was detected.
        seen[node] = False # Mark node as grey.
        for next_node in reverse_adj_list[node]:
            result = visit(next_node)
            if not result: 
                return False # Cycle was detected lower down.
        seen[node] = True # Mark node as black.
        output.append(node)
        return True

    if not all(visit(node) for node in reverse_adj_list):
        return ""

    return "".join(output)