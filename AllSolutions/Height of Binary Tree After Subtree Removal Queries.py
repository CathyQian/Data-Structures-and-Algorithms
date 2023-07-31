"""
Height of Binary Tree After Subtree Removal Queries

You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
 

Example 1:


Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
Output: [2]
Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).

Example 2:


Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
Output: [3,2,3,2]
Explanation: We have the following queries:
- Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
- Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
- Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
- Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
m == queries.length
1 <= m <= min(n, 104)
1 <= queries[i] <= n
queries[i] != root.val

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# brutal force, TLE (40 min)
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        allpaths, res = [], []
        self.findTreePaths(root, [], allpaths)
        length = [len(allpaths[i])-1 for i in range(len(allpaths))]
        for query in queries:
            l_copy = length.copy()
            # the following block is quite time-consuming
            for i, path in enumerate(allpaths):
                if query in path:
                    idx = path.index(query)
                    l_copy[i] = idx - 1
            res.append(max(l_copy))
        return res

    def findTreePaths(self, node, curpath, allpaths):
        if not node:
            return
        if node and not node.left and not node.right and curpath:
            allpaths.append(curpath + [node.val])
        else: # node with one or two child
            if node.left: 
                self.findTreePaths(node.left, curpath + [node.val], allpaths)
            if node.right:
                self.findTreePaths(node.right, curpath + [node.val], allpaths)

# optimized DFS, but hard to understand
import collections
class Solution:
    def treeQueries(self, root, queries):
        @lru_cache(None) # this line is needed, otherwise TLE; "@lru_cache(None)" is a Python decorator that caches the results of a function call. 
        # When the function is called with the same arguments again, it returns the cached result instead of recalculating it.
        def height(node):
            # height from node to leave
            if not node:
                return -1

            return 1 + max(height(node.left),height(node.right))
        
        # depth from root node to the current node
        dict1 = collections.defaultdict(int)
        def dfs(node, depth, max_val):
            if not node: 
                return 

            dict1[node.val] = max_val
            # these two lines are very smart
            dfs(node.left, depth + 1, max(max_val, depth + 1 + height(node.right)))
            dfs(node.right, depth + 1, max(max_val, depth + 1 + height(node.left)))

        dfs(root, 0, 0)

        return [dict1[i] for i in queries]
    
# Easy to understand
# DFS with detailed explanation: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/solutions/2757990/python-3-explanation-with-pictures-dfs/
class Solution:
    def treeQueries(self, R: Optional[TreeNode], Q: List[int]) -> List[int]:
        node_depth, node_height = collections.defaultdict(int), collections.defaultdict(int)

        def dfs(node, depth):
            # return height of node and update node depth along the way
            if not node:
                return -1
            node_depth[node.val] = depth
            cur = max(dfs(node.left, depth + 1), dfs(node.right, depth + 1)) + 1
            node_height[node.val] = cur
            return cur
        dfs(R, 0)

        cousins = collections.defaultdict(list) # Group nodes according to their depth. Keep the top 2 heights.
        for val, depth in node_depth.items():
            cousins[depth].append((node_height[val], val))
            cousins[depth].sort(reverse=True)
            while len(cousins[depth]) > 2:
                cousins[depth].pop()

        ans = []
        for q in Q:
            depth = node_depth[q]
            if len(cousins[depth]) == 1:  # No cousin, path length equals depth - 1.
                ans.append(depth - 1)
            elif cousins[depth][0][1] == q:  # The removed node has the largest height, look for the node with 2nd largest height.
                ans.append(cousins[depth][1][0] + depth)
            else:   # Look for the node with the largest height.
                ans.append(cousins[depth][0][0] + depth)
        return ans
    
