"""
Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5
  
Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        self.btPathHelper(root, [])
        return self.res
    
    def btPathHelper(self, node, curpath):
        if not node:
            return
        if not node.left and not node.right:
            curpath.append(str(node.val))
            self.res.append('->'.join(curpath))
        if node.left:
            self.btPathHelper(node.left, curpath + [str(node.val)])
        if node.right:
            self.btPathHelper(node.right, curpath + [str(node.val)])
            