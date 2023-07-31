"""
Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

      

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.

"""

# first thought is tree traversal via recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS, store each node along with their parent node
# time and space complexity O(n), n is the number of nodes in the tree
from collections import deque
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        d = deque([(None, root)])
        to_delete = set(to_delete)
        
        while d:
            parent, cur = d.popleft()
            if not cur: 
                continue
            
            if cur.val in to_delete:
                d.append((None, cur.left))
                d.append((None, cur.right))
                cur = None
            else: # cur.val not in to_delete
                # define the termination condition is when the parent is None and value isn't to be deleted
                if parent is None:
                    res.append(cur)
                
                if cur.left:
                    if cur.left.val in to_delete:
                        d.append((None, cur.left.left))
                        d.append((None, cur.left.right))
                        cur.left = None # needed to remove the connection
                    else:
                        d.append((cur, cur.left))
                
                if cur.right:
                    if cur.right.val in to_delete:
                        d.append((None, cur.right.left))
                        d.append((None, cur.right.right))
                        cur.right = None # needed to remove the connection
                    else:
                        d.append((cur, cur.right))
        
        return res
    
# DFS; the issue of the following solution is the tree structure is preserved (no node is actually deleted) ---- need to clarify with the interviewer
# time and space complexity O(n), n is the number of nodes in the tree

# wrong solution: tree is still intact
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete) # O(1) lookup 
        
        def fn(node, parent):
            """Return node upon deletion of required values."""
            if not node: 
                return
            if node.val in to_delete: 
                fn(node.left, None)
                fn(node.right, None)
                node = None
            else: 
                if not parent: 
                    ans.append(node)
                
                fn(node.left, node)
                fn(node.right, node)
            return
        
        ans = []
        fn(root, None)
        return ans 

# val in to_delete in tree removed
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete) # O(1) lookup 
        
        def fn(node, pval):
            """Return node upon deletion of required values."""
            if not node: 
                return None
            if node.val in to_delete: 
                node.left = fn(node.left, None)
                node.right = fn(node.right, None)
                return None
            else: 
                if not pval: 
                    ans.append(node)
                node.left = fn(node.left, node.val)
                node.right = fn(node.right, node.val)
                return node 
        
        ans = []
        fn(root, None)
        return ans 