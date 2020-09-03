"""
Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary 
tree is the length of the longest path between any two nodes in a tree. This path may or may not pass 
through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them. 

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxnodes = 0 # pay attention to the different definition of maxnodes and maxdiameter
        _ = self.diameterHelper(root)
        return max(0, self.maxnodes - 1) # in case it's negative 
                               
    def diameterHelper(self, node):
        # return max # nodes between node-left child and node-right child
        if not node:
            return 0
        l = self.diameterHelper(node.left)
        r = self.diameterHelper(node.right)
        self.maxnodes = max(self.maxnodes, l+r+1) # not l+r+1, to avoid confusion, we can count # of nodes 
                               
        return max(l,r) + 1 # not max(l, r)