"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least
one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.globalmax = - float('inf')
        _ = self.maxPathSumHelper(root)
        return self.globalmax
    
    def maxPathSumHelper(self, node):
        # max path sum start at node
        if root is None:
            return 0
        
        left = max(self.maxPathSumHelper(node.left), 0)
        right = max(self.maxPathSumHelper(node.right), 0)
        
        self.globalmax = max(left + node.val + right, self.globalmax)
        
        return max(left, right) + node.val
    